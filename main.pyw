import cv2
import time
import datetime
import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()
#environment variables

REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

cap = cv2.VideoCapture(1)
#change the number depending on which camera you will use, usually it's either 0 or 1

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTERR_DETECTION  = 3

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"jpeg")


while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    bodies = face_cascade.detectMultiScale(gray, 1.1, 4)
    current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M")


    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False
        else:
            detection= True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M")
            out = cv2.VideoWriter(f"{current_time}.png", fourcc, 15, frame_size)
            print("Press 'Q' to Exit")
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTERR_DETECTION:
                detection = False
                timer_started = False
                out.release()
        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)

    ##################### gDrive Upload ##########################        
        authorization_url = "https://oauth2.googleapis.com/token"
        params = {
                "grant_type": "refresh_token",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "refresh_token": REFRESH_TOKEN
        }

        r = requests.post(authorization_url, data=params)

        access_token = None

        if r.ok:
            access_token = r.json()['access_token']
        
        headers = {"Authorization": f"Bearer {access_token}"}
        para = {
        "name": f"{current_time}.png",
        }
        files = {
            'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
            'file': open(f"{current_time}.png", "rb")
        }
        r = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=headers,
            files=files
        )
        print(r.text)
        ##################### gDrive Upload ##########################     
        break

out.release()
cap.release()
cv2.destroyAllWindows()
