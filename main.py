import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import yt_dlp

def download_video():
    url = url_entry.get()
    download_type = download_type_var.get()

    ydl_opts = {
        'format': 'bestaudio/best' if download_type == "audio" else 'bestvideo+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '128',
        }] if download_type == "audio" else [],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"{download_type.capitalize()} downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("630x360")


# background image load
try:
    background_image = Image.open(r"C:\Users\seren\OneDrive\Desktop\vscode\python\background.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)
except Exception as e:
    messagebox.showerror("Error", f"Failed to load background image: {str(e)}")

url_label = tk.Label(root, text="YouTube URL:", bg="#e1e1e1", font=("Helvetica", 14), borderwidth=1, relief="solid")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50, font=("Helvetica", 12))
url_entry.pack(pady=5)

download_type_var = tk.StringVar(value="video")  # Default to video

video_radio = tk.Radiobutton(root, text="Download Video", variable=download_type_var, value="video", bg="#e1e1e1", font=("Helvetica", 12), borderwidth=1, relief="solid")
video_radio.pack(anchor='w', padx=20, pady=5)

audio_radio = tk.Radiobutton(root, text="Download Audio", variable=download_type_var, value="audio", bg="#e1e1e1", font=("Helvetica", 12), borderwidth=1, relief="solid")
audio_radio.pack(anchor='w', padx=20, pady=5)

download_button = tk.Button(root, text="Download", command=download_video, bg="#4CAF50", fg="white", font=("Helvetica", 14))
download_button.pack(pady=20)

root.mainloop()