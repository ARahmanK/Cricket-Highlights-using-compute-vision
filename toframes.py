import cv2, os
from tkinter import *
from tkinter.ttk import *
import time


class ToFrames:

    def read_video(self, path):
        frame_path = '/home/ark/FYP1/pytorch/Frames'
        cap = cv2.VideoCapture(path)  # capture video from given path
        frame_no = 1  # intilize variable frame name
        fps = cap.get(5)  # get the fps of frame
        window = self.frame_window()
        while cap.isOpened():
            ret, frame = cap.read()  # Reading video
            # ret return bool
            # frame return one frame of video
            if ret == False:
                print('ret is false')
                break;
            current_frame = cap.get(1)  # return integer value and tell current number of frame of video
            if current_frame % ((fps)/2) == 0:  # save 2 frame of each sec
                print('frame # ', frame_no)
                self.step(window[0], window[1], frame_no)
                cv2.imwrite(os.path.join(frame_path, 'Frame' + str(frame_no) + '.jpg'), frame)
                frame_no += 1
        cap.release()
        self.frame_window()
        cv2.destroyAllWindows()
        return [frame_no, frame_path]

    def frame_window(self):
        print('generating frames window')
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
        return [pb1,frames_root]
        # frames_root.destroy()

    def step(self, pb1, frames_root, frame):
        val = (int(frame) / 2880) * 100
        frames_root.update_idletasks()
        pb1['value'] = val
        # time.sleep(.0001)
        if frame == '2880':
            frames_root.destroy()
# tf = ToFrames()
# tf.read_video()
