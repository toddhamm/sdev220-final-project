# imports

# gui is built in customtkinter
import customtkinter as ctk
from tkinter import filedialog  # Required for the file explorer window

# pathlib and os to set the default directory of the file dialog menu to desktop
from pathlib import Path
import os

# csv for reading the opened csv files
import csv

# Set the application window theme
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("CustomTkinter File Opener")
        self.geometry("1000x600")
        
        # Create a modern button to trigger the file dialog
        self.button = ctk.CTkButton(
            self, 
            text="Open File", 
            command=self.open_file_dialog
        )
        self.button.pack(pady=40, padx=20)
        
        # Create a label to display the chosen file path
        self.label = ctk.CTkLabel(self, text="No file selected", wraplength=350)
        self.label.pack(pady=10)

        # Target the Desktop directory safely on Windows, Mac, or Linux
        self.desktop_dir = Path.home() / "Desktop"

    def open_file_dialog(self):
        # Open the standard system file dialog
        file_path = filedialog.askopenfilename(
            title="Select a File",
            initialdir=self.desktop_dir,
            filetypes=[
                ("CSV", "*.csv"),
            ]
        )
        
        # Check if the user selected a file or canceled the window
        if file_path:
            self.label.configure(text=f"Selected: {file_path}")
            print(f"File loaded from: {file_path}")

            # open the file and display contents on screen

            # Open the file using a context manager (auto-closes the file)
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                
                # Optional: Skip the header row if you don't want to print it
                header = next(reader) 
                
                for row in reader:
                    print(row)

        else:
            self.label.configure(text="File selection canceled")

    # open the file

if __name__ == "__main__":
    app = App()
    app.mainloop()