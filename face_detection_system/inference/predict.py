import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    return "Predicted: Female" if prediction[0] <= 0.5 else "Predicted: Male"

def predict_video(video_path):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        return "Error: Could not open video."

    predictions = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Preprocess the frame (resize, normalize, etc.)
        frame_resized = cv2.resize(frame, (128, 128))
        frame_array = frame_resized.astype('float32') / 255.0
        frame_array = np.expand_dims(frame_array, axis=0)  # Add batch dimension

        # Make predictions
        prediction = model.predict(frame_array)
        if prediction[0] <= 0.5:
            predictions.append("Female")
        else:
            predictions.append("Male")
    
    cap.release()
    
    # Return the most common prediction
    if predictions:
        return max(set(predictions), key=predictions.count)
    else:
        return "No predictions made."

if __name__ == "__main__":
    img_path = input("Enter image path: ")
    print(predict_image(img_path))
