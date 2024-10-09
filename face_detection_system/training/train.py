import os
import sys

# Add the parent directory to sys.path to locate 'models' and other directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.download_dataset import download_dataset
from data_preprocessing.preprocess import load_and_preprocess_data
from models.model import create_model

import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Step 1: Download dataset
dataset_path = download_dataset()  # This will download the dataset and return the path
print("Dataset path:", dataset_path)

# Step 2: Load and preprocess data
img_size = (128, 128)
train_gen, val_gen = load_and_preprocess_data(dataset_path, img_size)

# Step 3: Create the model
model = create_model(input_shape=(128, 128, 3))

# Step 4: Define callbacks (optional)
early_stopping = EarlyStopping(monitor='val_loss', patience=5)
checkpoint = ModelCheckpoint('best_model.keras', save_best_only=True, monitor='val_loss')  # Use .keras extension

# Step 5: Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 6: Train the model
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=10,
    callbacks=[early_stopping, checkpoint]
)

# Step 7: Save the final model as 'gender_detection_model.keras'
model.save('gender_detection_model.keras')  # Use .keras extension

# Step 8: Evaluate and print final validation accuracy
val_loss, val_accuracy = model.evaluate(val_gen)
print(f"Final validation accuracy: {val_accuracy:.4f}")

# Step 9: Plot the training results and save accuracy and loss graphs
def plot_training_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    
    epochs = range(len(acc))
    
    # Plot accuracy
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(epochs, acc, label='Training Accuracy')
    plt.plot(epochs, val_acc, label='Validation Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.legend()
    plt.savefig('accuracy_plot.png')  # Save accuracy plot as PNG file
    plt.close()  # Close the plot to save resources
    
    # Plot loss
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 2)
    plt.plot(epochs, loss, label='Training Loss')
    plt.plot(epochs, val_loss, label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.legend()
    plt.savefig('loss_plot.png')  # Save loss plot as PNG file
    plt.close()  # Close the plot to save resources

# Step 10: Plot the training results
plot_training_history(history)
