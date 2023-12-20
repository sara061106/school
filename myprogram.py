from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")

        self.input_image_path = None
        self.output_image_path = None

        # Create buttons
        self.btn_add_photo = tk.Button(root, text="Add Photo", command=self.load_image)
        self.btn_process_photo = tk.Button(root, text="Process Photo", command=self.process_image)
        self.btn_save_photo = tk.Button(root, text="Save Processed Photo", command=self.save_image)

        # Create labels
        self.lbl_input_image = tk.Label(root, text="Input Image:")
        self.lbl_output_image = tk.Label(root, text="Processed Image:")

        # Set up the layout
        self.lbl_input_image.grid(row=0, column=0, padx=10, pady=5)
        self.lbl_output_image.grid(row=0, column=1, padx=10, pady=5)
        self.btn_add_photo.grid(row=1, column=0, padx=10, pady=5)
        self.btn_process_photo.grid(row=2, column=0, padx=10, pady=5)
        self.btn_save_photo.grid(row=3, column=0, padx=10, pady=5)

    def load_image(self):
        file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg;*.png;*.gif")])
        if file_path:
            self.input_image_path = file_path
            self.lbl_input_image.config(text=f"Input Image: {file_path}")
            self.display_image(file_path, 0, 1)

    def process_image(self):
        if self.input_image_path:
            new_size = (300, 200)
            img = Image.open(self.input_image_path)
            resized_img = img.resize(new_size)
            self.output_image_path = "processed_image.jpg"
            resized_img.save(self.output_image_path)
            self.lbl_output_image.config(text=f"Processed Image: {self.output_image_path}")
            self.display_image(self.output_image_path, 0, 1)

    def save_image(self):
        if self.output_image_path:
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
            if save_path:
                self.output_image_path = save_path
                self.lbl_output_image.config(text=f"Processed Image: {self.output_image_path}")
                Image.open(self.output_image_path).save(self.output_image_path)

    def display_image(self, image_path, row, column):
        img = Image.open(image_path)
        img.thumbnail((100, 100))
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(self.root, image=img)
        panel.image = img
        panel.grid(row=row, column=column, padx=10, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
