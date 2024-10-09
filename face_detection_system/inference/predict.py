import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

def predict_image(img_path):
    model = load_model('/workspaces/Gender_Detection_System_ML/face_detection_system/models/gender_detection_model.keras')  # Load the .keras model

    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    if prediction[0] > 0.5:
        print("Predicted: Female")
    else:
        print("Predicted: Male")

if __name__ == "__main__":
    img_path = input("Enter image path: ")
    predict_image(img_path)
