import tkinter as tk
from tkinter import filedialog, messagebox
from organizer.core import organize_folder

def start_app():
    root = tk.Tk()
    root.title("File Organizer Pro")
    root.geometry("400x200")

    label = tk.Label(root, text="Select a folder to organize", font=("Arial", 12))
    label.pack(pady=20)

    def choose_folder():
        path = filedialog.askdirectory()
        if path:
            try:
                organize_folder(path)
                messagebox.showinfo("Success", "Folder organized successfully!")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    btn = tk.Button(root, text="Choose Folder", command=choose_folder, width=20)
    btn.pack(pady=10)

    root.mainloop()
