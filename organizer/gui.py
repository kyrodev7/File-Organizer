import tkinter as tk
from tkinter import filedialog, messagebox
from organizer.core import organize_folder

def start_app():
    root = tk.Tk()
    root.title("File Organizer Pro")
    root.geometry("400x250")

    label = tk.Label(root, text="Select a folder to organize", font=("Arial", 12))
    label.pack(pady=20)

    label2 = tk.Label(root, text="Ready", font=("Arial", 12))
    label2.pack(pady=20)

    current_theme = "light"

    def enable_dark_mode():
      nonlocal current_theme
      if current_theme == "light":
         root.config(bg="black")  
         label.config(bg="black", fg="white")
         label2.config(bg="black", fg="white")
         btn.config(bg="black", fg="white")
         dark_button.config(bg="black", fg="white", text="Light Mode")
         current_theme = "dark"
      else:
         root.config(bg="white")  
         label.config(bg="white", fg="black")
         label2.config(bg="white", fg="black")
         btn.config(bg="white", fg="black")
         dark_button.config(bg="white", fg="black", text="Dark Mode")
         current_theme = "light"

    def choose_folder():
        path = filedialog.askdirectory()
        if path:
            try:
                label2.config(text="Organizing...")
                organize_folder(path)
                messagebox.showinfo("Success", "Folder organized successfully!")
                label2.config(text="Organized!")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    btn = tk.Button(root, text="Choose Folder", command=choose_folder, width=20)
    btn.pack(pady=10)

    dark_button = tk.Button(root, text="Dark Mode", command=enable_dark_mode)
    dark_button.pack()

    root.mainloop()
