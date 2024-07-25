import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

def browse_input():
    input_dir = filedialog.askdirectory()
    input_path.set(input_dir)

def organize_files():
    input_dir = input_path.get()

    if not input_dir:
        messagebox.showerror("Error", "Please select the input directory")
        return

    for root, _, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(root, file)
            mod_time = os.path.getmtime(file_path)
            mod_date = datetime.fromtimestamp(mod_time)
            
            year = mod_date.strftime('%Y')
            month = mod_date.strftime('%B')
            
            year_folder = os.path.join(input_dir, year)
            month_folder = os.path.join(year_folder, month)
            
            if not os.path.exists(month_folder):
                os.makedirs(month_folder)
                
            shutil.move(file_path, month_folder)

    messagebox.showinfo("Success", "Files have been organized successfully!")

root = tk.Tk()
root.title("File Organizer")
input_path = tk.StringVar()
tk.Label(root, text="Select Input Directory:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=input_path, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_input).grid(row=0, column=2, padx=10, pady=10)
tk.Button(root, text="Organize Files", command=organize_files).grid(row=1, column=1, pady=20)

root.mainloop()
