import socket
import cv2
import numpy as np
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("server_ip_address", 12345))  # Replace with the server's IP address

cap = cv2.VideoCapture(0)  # 0 for the default camera

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))  # Resize the frame to a standard size
    encoded_frame = cv2.imencode('.jpg', frame)[1].tobytes()
    client.send(encoded_frame)
#Create threads for sending and receiving  
send_thread = threading.Thread(target=send_frames)
receive_thread = threading.Thread(target=receive_frames)
send_thread.start()
receive_thread.start()    