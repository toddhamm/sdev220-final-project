import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("CustomTkinter Example")
app.geometry("1000x600")

label = ctk.CTkLabel(app, text="Modern Python UI")
label.pack(pady=20)

btn = ctk.CTkButton(app, text="Click Me", command=lambda: label.configure(text="Button Clicked!"))
btn.pack(pady=10)

app.mainloop()