from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_and_preprocess_data(dataset_path, img_size=(128, 128)):
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

    train_gen = datagen.flow_from_directory(
        dataset_path,
        target_size=img_size,
        batch_size=32,
        class_mode='binary',
        subset='training'
    )
    
    val_gen = datagen.flow_from_directory(
        dataset_path,
        target_size=img_size,
        batch_size=32,
        class_mode='binary',
        subset='validation'
    )
    
    return train_gen, val_gen
