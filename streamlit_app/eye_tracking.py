import streamlit as st
import cv2
import mediapipe as mp

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)

# Title of the app
st.title('Eye Tracking App')

# Upload video file
video_file = st.file_uploader('Upload a video', type=['mp4', 'mov', 'avi'])

if video_file is not None:
    # Read the video file
    video_file_path = f'./{video_file.name}'
    with open(video_file_path, 'wb') as f:
        f.write(video_file.getbuffer())
    cap = cv2.VideoCapture(video_file_path)
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the BGR image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)

        # Draw face detections
        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display image in Streamlit
        stframe.image(frame, channels='RGB')

    cap.release()