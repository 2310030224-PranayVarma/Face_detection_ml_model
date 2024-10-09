import cv2
from tensorflow.keras.models import load_model
import numpy as np

def predict_webcam():
    model = load_model('/workspaces/Gender_Detection_System_ML/face_detection_system/models/gender_detection_model.keras')  # Load the .keras model
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        img = cv2.resize(frame, (128, 128))
        img_array = np.expand_dims(img, axis=0) / 255.0
        
        prediction = model.predict(img_array)
        label = "Female" if prediction[0] <= 0.5 else "Male"
        
        cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Webcam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    predict_webcam()
