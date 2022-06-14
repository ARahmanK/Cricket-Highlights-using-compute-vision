from tkinter import *
from tkinter.ttk import *
import time


class ProgressBars:
    def frame_window(self,frame):
        frames_root = Tk()
        # Adjust size
        frames_root.title('Generating Frames')
        frames_root.geometry("400x150")
        frames_root.minsize(400, 150)
        frames_root.maxsize(400, 150)
        frames_root.config(bg="white")

        text = Label(frames_root, text="Creating Frames", font=('times', 15), background='white')
        text.pack(pady=25)
        style = Style()
        style.theme_use('alt')
        style.configure("red.Horizontal.TProgressbar", background='green')
        pb1 = Progressbar(frames_root, orient=HORIZONTAL, style="red.Horizontal.TProgressbar", length=390,
                          mode='determinate')
        pb1.pack(expand=True)
        self.step(pb1, frames_root, frame)
        frames_root.destroy()

    def step(self, pb1, frames_root, frame):
        val = (int(frame) / 2768) * 100
        frames_root.update_idletasks()
        pb1['value'] = val
        time.sleep(.0001)