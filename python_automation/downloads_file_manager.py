# Created by Nardelli17 
# Date 31-08-2024.

import os
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def get_files_in_downloads():
    downloads_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    files = [
        os.path.join(downloads_folder, f) for f in os.listdir(downloads_folder)
        if os.path.isfile(os.path.join(downloads_folder, f))
    ]
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return files

def delete_file(file_path):
    try:
        os.remove(file_path)
        messagebox.showinfo("Success", f"{os.path.basename(file_path)} has been deleted.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not delete the file: {e}")

def refresh_file_list(filter_text=""):
    for widget in file_frame.winfo_children():
        widget.destroy()

    files = get_files_in_downloads()
    
    if filter_text:
        files = [f for f in files if filter_text.lower() in os.path.basename(f).lower()]
    
    file_count_label.config(text=f"Total files: {len(files)}")
    
    for index, file in enumerate(files):
        file_size = os.path.getsize(file) / (1024 * 1024)
        file_mtime = time.ctime(os.path.getmtime(file))
        file_name = os.path.basename(file)
        
        file_label = tk.Label(file_frame, text=f"{file_name}\n{file_size:.2f} MB | {file_mtime}",
                              anchor="center", bg="#f0f0f0", font=("Arial", 10))
        file_label.grid(row=index * 2, column=0, padx=10, pady=5, sticky="ew")
        
        delete_button = tk.Button(file_frame, text="Delete", command=lambda f=file: on_delete_file(f),
                                  bg="#ff4d4d", fg="white", font=("Arial", 9, "bold"))
        delete_button.grid(row=index * 2 + 1, column=0, pady=5)
        
        separator = tk.Frame(file_frame, height=1, bd=1, relief="sunken", bg="#e0e0e0")
        separator.grid(row=index * 2 + 2, column=0, sticky="ew", padx=10, pady=5)

    file_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def on_delete_file(file_path):
    if messagebox.askyesno("Confirmation", f"Are you sure you want to delete {os.path.basename(file_path)}?"):
        delete_file(file_path)
        refresh_file_list(search_var.get())

def on_search_change(*args):
    refresh_file_list(search_var.get())

root = tk.Tk()
root.title("Downloads File Manager")
root.geometry("490x700")
root.configure(bg="#ffffff")

file_count_label = tk.Label(root, text="Total files: 0", font=("Arial", 14, "bold"), bg="#ffffff")
file_count_label.pack(pady=10)

search_var = tk.StringVar()
search_var.trace_add("write", on_search_change)
search_entry = tk.Entry(root, textvariable=search_var, font=("Arial", 12), width=50)
search_entry.pack(pady=10)

frame_container = tk.Frame(root, bg="#ffffff")
frame_container.pack(fill="both", expand=True)

canvas = tk.Canvas(frame_container, bg="#ffffff")
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

file_frame = tk.Frame(canvas, bg="#ffffff")
canvas.create_window((0, 0), window=file_frame, anchor="nw")

refresh_button = tk.Button(root, text="Refresh List", command=lambda: refresh_file_list(search_var.get()), bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
refresh_button.pack(pady=20)

root.mainloop()
