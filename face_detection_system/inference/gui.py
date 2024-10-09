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
root.title("Face Detection - Male/Female Classifier")
root.geometry("300x150")

# Create an upload button
btn = tk.Button(root, text="Upload Image", command=upload_image)
btn.pack(pady=20)

# Run the application
root.mainloop()
