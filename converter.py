import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def mp4_to_mp3():
    file_path = filedialog.askopenfilename(title="Select MP4 File", filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        mp3_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if mp3_path:
            video = VideoFileClip(file_path)
            audio = video.audio
            audio.write_audiofile(mp3_path)
            mp4_label.config(text=f"Selected MP4 file: {file_path}")
            mp3_label.config(text=f"MP3 file saved to: {mp3_path}")

root = tk.Tk()
root.title("MP4 to MP3 Converter")

mp4_label = tk.Label(root, text="Selected MP4 file: ")
mp4_label.pack(pady=10)

mp3_label = tk.Label(root, text="MP3 file saved to: ")
mp3_label.pack(pady=10)

convert_button = tk.Button(root, text="Convert MP4 to MP3", command=mp4_to_mp3)
convert_button.pack(pady=10)

root.mainloop()
