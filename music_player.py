import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")

        self.current_track = None
        self.playlist = []

        pygame.init()

        self.create_widgets()

    def create_widgets(self):
        self.track_label = tk.Label(self.root, text="Music Player", font=("Helvetica", 20))
        self.track_label.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Song", command=self.add_song)
        self.add_button.pack(pady=5)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_song)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_song)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_song)
        self.stop_button.pack(pady=5)

    def add_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if song_path:
            song_title = os.path.basename(song_path)
            self.playlist.append((song_title, song_path))
            self.track_label.config(text=f"Now Playing: {song_title}")

    def play_song(self):
        if self.playlist:
            song_title, song_path = self.playlist[0]
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            self.current_track = 0

    def pause_song(self):
        if self.current_track is not None:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()

    def stop_song(self):
        if self.current_track is not None:
            pygame.mixer.music.stop()
            self.current_track = None
            self.track_label.config(text="Music Player")

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()
