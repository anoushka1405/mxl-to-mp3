import subprocess
import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import platform

CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

config = load_config()
MUSESCORE_PATH = config.get("musescore_path", "")

def update_status(text):
    status_label.config(text=text)

def open_folder(path):
    system = platform.system()
    if system == "Darwin":       # macOS
        subprocess.run(["open", path])
    elif system == "Windows":    # Windows
        subprocess.run(["explorer", path])
    else:                        # Linux variants
        subprocess.run(["xdg-open", path])

def convert_mxl_to_mp3(mxl_path):
    root.after(0, update_status, "Converting... Please wait.")
    output_folder = "converted_mp3s"
    os.makedirs(output_folder, exist_ok=True)

    filename = os.path.splitext(os.path.basename(mxl_path))[0] + ".mp3"
    output_mp3 = os.path.join(output_folder, filename)

    try:
        subprocess.run([MUSESCORE_PATH, "-o", output_mp3, mxl_path], check=True)
        root.after(0, update_status, f"Conversion done! Saved as:\n{output_mp3}")
        open_folder(output_folder)
    except subprocess.CalledProcessError as e:
        root.after(0, update_status, "Conversion failed.")
        messagebox.showerror("Conversion Error", str(e))

def start_conversion_thread(mxl_path):
    thread = threading.Thread(target=convert_mxl_to_mp3, args=(mxl_path,))
    thread.start()

def start_conversion():
    mxl_path = entry_path.get()
    if not mxl_path:
        messagebox.showwarning("Input Needed", "Please select a .mxl file first.")
        return
    if not MUSESCORE_PATH or not os.path.isfile(MUSESCORE_PATH):
        messagebox.showerror("Configuration Error", "Musescore path is not set or invalid! Please update config.json.")
        return
    start_conversion_thread(mxl_path)

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("MusicXML files", "*.mxl"), ("All files", "*.*")])
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)
        status_label.config(text="")

# Tkinter UI setup unchanged...

root = tk.Tk()
root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

root.title("MusicXML to MP3 Converter")
root.geometry("450x180")

tk.Label(root, text="Select MusicXML (.mxl) file:").pack(pady=5)
entry_path = tk.Entry(root, width=50)
entry_path.pack(pady=5)

btn_browse = tk.Button(root, text="Browse", command=browse_file)
btn_browse.pack(pady=5)

btn_convert = tk.Button(root, text="Convert to MP3", command=start_conversion)
btn_convert.pack(pady=10)

status_label = tk.Label(root, text="", fg="blue")
status_label.pack(pady=5)

root.mainloop()

