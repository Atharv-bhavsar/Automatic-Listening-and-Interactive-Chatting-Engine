import tkinter as tk
from PIL import Image, ImageTk
import cv2
import pygame


def play_audio():
    # Start playing the audio
    pygame.mixer.music.play()


class VideoPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Player")
        self.master.bind("<Configure>", self.on_configure)
        self.master.attributes("-fullscreen", False)

        # Hide maximize, minimize, and close buttons
        self.master.overrideredirect(True)

        # Open video capture
        self.cap = cv2.VideoCapture('Media/splash_screen.mp4')
        if not self.cap.isOpened():
            print("Error: Unable to open video file.")
            self.master.destroy()
            return

        # Get video properties
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Create label to display video
        self.video_label = tk.Label(self.master)
        self.video_label.pack(expand=True, fill=tk.BOTH)

        # Initialize Pygame for audio playback
        pygame.mixer.init()

        # Load the audio file
        pygame.mixer.music.load("Media/alice_audio.mp3")

        # Schedule audio playback with a delay
        self.master.after(3000, play_audio)

        # Start playing video
        self.play_video()

    def play_video(self):
        ret, frame = self.cap.read()
        if ret:
            # Resize frame to fit window size
            frame = cv2.resize(frame, (self.width, self.height))

            # Convert frame from BGR to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert frame to ImageTk format
            img = Image.fromarray(rgb_frame)
            img_tk = ImageTk.PhotoImage(image=img)

            # Update label with new frame
            self.video_label.config(image=img_tk)
            self.video_label.img = img_tk

            # Repeat after delay (milliseconds)
            self.master.after(30, self.play_video)
        else:
            # Release video capture and close window when video ends
            self.cap.release()
            self.master.destroy()

    def on_configure(self, event):
        if event.width == self.master.winfo_screenwidth() and event.height == self.master.winfo_screenheight():
            self.master.attributes("-fullscreen", True)
        else:
            self.master.attributes("-fullscreen", False)


def start():
    root = tk.Tk()
    # Calculate the center position of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 800  # set your desired window width
    window_height = 400  # set your desired window height
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    VideoPlayerApp(root)
    root.mainloop()



start()
