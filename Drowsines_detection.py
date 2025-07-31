*Drowsiness pythons code* 🖊️

import cv2
import mediapipe as mp
import serial
import time

# Serial communication with Arduino
arduino = serial.Serial('COM3', 9600)  # Replace COM3 with your port
time.sleep(2)

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        # Simulate drowsy condition (for testing)
        print("AWAKE")
        arduino.write(b'0')  # Send 0 to Arduino
    else:
        print("SLEEP")
        arduino.write(b'1')  # Send 1 to Arduino

    cv2.imshow("Driver Monitor", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
