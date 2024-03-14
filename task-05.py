import cv2

class FaceRecognizer:
    def __init__(self):
        # Loading pre-trained face detection model
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def recognize_face(self, face):
        print("Face recognized!")

    def detect_and_recognize_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            self.recognize_face(face)
            # Draw rectangle around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        return frame

    def process_video(self, video_path):
        # Open the video file
        cap = cv2.VideoCapture(video_path)

        # Check if the video opened successfully
        if not cap.isOpened():
            print("Error: Unable to open video.")
            return

        # Read and process frames
        while True:
            ret, frame = cap.read()

            if not ret:
                break

            # Detect and recognize faces in the frame
            processed_frame = self.detect_and_recognize_faces(frame)

            # Display the processed frame
            cv2.imshow('Face Detection', processed_frame)

            # Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = 'video.mp4'
    recognizer = FaceRecognizer()
    recognizer.process_video(video_path)
