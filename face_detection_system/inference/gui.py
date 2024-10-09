import tkinter as tk
from tkinter import filedialog, messagebox
from predict import predict_image, predict_video  # Import both functions
import cv2

def upload_image():
    if file_path := filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]
    ):
        result = predict_image(file_path)
        messagebox.showinfo("Prediction Result", result)

def upload_video():
    if file_path := filedialog.askopenfilename(
        filetypes=[("Video Files", "*.mp4;*.avi")]
    ):
        result = predict_video(file_path)
        messagebox.showinfo("Prediction Result", result)

def use_camera():
    cap = cv2.VideoCapture(0)  # Use the default camera
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not open webcam")
        return
    
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("temp_image.jpg", frame)  # Save the captured frame as an image
        result = predict_image("temp_image.jpg")  # Predict using the saved image
        messagebox.showinfo("Prediction Result", result)
    else:
        messagebox.showerror("Error", "Failed to capture image")
    
    cap.release()

# Create the main window
root = tk.Tk()
root.title("Gender Detection - Male/Female Classifier")
root.geometry("400x300")
root.resizable(False, False)  # Disable resizing for better layout

# Create buttons for each option
btn_frame = tk.Frame(root)
btn_frame.pack(pady=30)

btn_image = tk.Button(btn_frame, text="Upload Image", command=upload_image, width=20)
btn_image.pack(pady=10)

btn_video = tk.Button(btn_frame, text="Upload Video", command=upload_video, width=20)
btn_video.pack(pady=10)

btn_camera = tk.Button(btn_frame, text="Use Camera", command=use_camera, width=20)
btn_camera.pack(pady=10)

# Run the application
root.mainloop()
