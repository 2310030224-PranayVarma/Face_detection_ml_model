from tensorflow.keras.models import load_model
from data_preprocessing.preprocess import load_and_preprocess_data
from dataset.download_dataset import download_dataset

def evaluate_model():
    dataset_path = download_dataset()
    _, val_gen = load_and_preprocess_data(dataset_path)

    model = load_model('face_detection_model.h5')
    loss, accuracy = model.evaluate(val_gen)
    
    print(f"Validation Loss: {loss}")
    print(f"Validation Accuracy: {accuracy}")

if __name__ == "__main__":
    evaluate_model()
