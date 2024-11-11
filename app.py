from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Union
from pyannote.audio import Model
from pyannote.audio.pipelines import VoiceActivityDetection, OverlappedSpeechDetection

app = FastAPI()

# Load the segmentation model
model = Model.from_pretrained(
    "pyannote/segmentation-3.0", 
    use_auth_token="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"
)

# Define the response format
class VADOSDResponse(BaseModel):
    status: str
    data: Union[List[Dict[str, float]], None]
    error: Union[str, None]

@app.get("/process-audio", response_model=VADOSDResponse)
async def process_audio():
    try:
        # Voice Activity Detection (VAD)
        vad_pipeline = VoiceActivityDetection(segmentation=model)
        vad_hyperparameters = {
            "min_duration_on": 0.0,
            "min_duration_off": 0.0
        }
        vad_pipeline.instantiate(vad_hyperparameters)
        vad = vad_pipeline(r"C:\\Users\\sohad\\OneDrive\\Desktop\\Python\\BacBon\\codes\\F_0101_10y4m_1.wav")
        
        # Collect VAD results
        vad_data = [
            {"start": segment.start, "stop": segment.end, "label": label}
            for segment, _, label in vad.itertracks(yield_label=True)
        ]
        
        # Overlapped Speech Detection (OSD)
        osd_pipeline = OverlappedSpeechDetection(segmentation=model)
        osd_hyperparameters = {
            "min_duration_on": 0.0,
            "min_duration_off": 0.0
        }
        osd_pipeline.instantiate(osd_hyperparameters)
        osd = osd_pipeline(r"C:\\Users\\sohad\\OneDrive\\Desktop\\Python\\BacBon\\codes\\F_0101_10y4m_1.wav")
        
        # Collect OSD results
        osd_data = [
            {"start": segment.start, "stop": segment.end, "label": label}
            for segment, _, label in osd.itertracks(yield_label=True)
        ]
        
        # Combine results
        data = {
            "VAD": vad_data,
            "OSD": osd_data
        }

        return VADOSDResponse(status="success", data=data, error=None)
    except Exception as e:
        return VADOSDResponse(status="error", data=None, error=str(e))

