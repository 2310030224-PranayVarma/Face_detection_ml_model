from training.train import train
from evaluation.evaluate import evaluate_model
from inference.predict import predict_image

def main():
    print("Choose an option:")
    print("1. Train the model")
    print("2. Evaluate the model")
    print("3. Predict using an image")

    choice = input("Enter your choice: ")

    if choice == "1":
        train()
    elif choice == "2":
        evaluate_model()
    elif choice == "3":
        img_path = input("Enter image path: ")
        predict_image(img_path)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
