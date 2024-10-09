### Face_detection_ml_model

# Face Detection System

This project is a Face Detection System to classify faces as either male or female. The model uses a CNN (Convolutional Neural Network) trained on the Male and Female Faces Dataset from Kaggle.

## Project Structure

- **dataset/**: Script to download the dataset using kagglehub.
- **data_preprocessing/**: Scripts to handle data cleaning, augmentation, and splitting.
- **models/**: Contains the model architecture.
- **training/**: Scripts to train the model.
- **evaluation/**: Scripts to evaluate the model and generate metrics.
- **inference/**: Scripts for predictions, GUI interface, and webcam predictions.
- **notebooks/**: Jupyter notebooks for exploratory data analysis and model training.
- **requirements.txt**: List of dependencies.
- **main.py**: Main script to run the full pipeline.

## How to Run the Project

1. Download the dataset:
   ```bash
   python dataset/download_dataset.py
