# instantiate the model
from pyannote.audio import Model
model = Model.from_pretrained(
  "pyannote/segmentation-3.0", 
  use_auth_token="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")
from pyannote.audio.pipelines import VoiceActivityDetection
pipeline = VoiceActivityDetection(segmentation=model)
HYPER_PARAMETERS = {
  # remove speech regions shorter than that many seconds.
  "min_duration_on": 0.0,
  # fill non-speech regions shorter than that many seconds.
  "min_duration_off": 0.0
}
pipeline.instantiate(HYPER_PARAMETERS)
vad = pipeline(r"C:\\Users\\sohad\\OneDrive\\Desktop\\Python\\BacBon\\codes\\F_0101_10y4m_1.wav")
# `vad` is a pyannote.core.Annotation instance containing speech regions
from pyannote.audio.pipelines import OverlappedSpeechDetection
pipeline = OverlappedSpeechDetection(segmentation=model)
HYPER_PARAMETERS = {
  # remove overlapped speech regions shorter than that many seconds.
  "min_duration_on": 0.0,
  # fill non-overlapped speech regions shorter than that many seconds.
  "min_duration_off": 0.0
}
pipeline.instantiate(HYPER_PARAMETERS)
osd = pipeline(r"C:\\Users\\sohad\\OneDrive\\Desktop\\Python\\BacBon\\codes\\F_0101_10y4m_1.wav")
# `osd` is a pyannote.core.Annotation instance containing overlapped speech regions

print("VAD contains segments:", len(vad))
print("OSD contains segments:", len(osd))



