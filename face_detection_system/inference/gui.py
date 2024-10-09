import tkinter as tk
from tkinter import filedialog, messagebox
from predict import predict_image

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:  # Check if a file was selected
        result = predict_image(file_path)
        messagebox.showinfo("Prediction Result", result)

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
