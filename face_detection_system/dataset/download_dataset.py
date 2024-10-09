import os

def download_dataset():
    # Path to the dataset folder
    dataset_dir = os.path.join(os.path.dirname(__file__), 'Male and Female face dataset')

    # Check if the dataset directory exists
    if os.path.exists(dataset_dir):
        print("Dataset found at:", dataset_dir)
        return dataset_dir  # Return the path to the dataset directory
    else:
        raise FileNotFoundError("Dataset folder not found!")

