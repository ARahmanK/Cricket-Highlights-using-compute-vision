import time
from tkinter.filedialog import askopenfile
import os, toframes, model_highlights, clip_cutting
from tkinter import *


def open_file(check_box):
    if check_box[0] or check_box[1] or check_box[2]:
        file_path = askopenfile(mode='r', filetypes=[('Video Files', '*mp4')])
        if file_path is not None:
            video_address = file_path.name
            toframe = toframes.ToFrames()

            # Creating objects of classes to get access of method
            model = model_highlights.Model()
            clip = clip_cutting.ClipCutting()
            frame_no = toframe.read_video(video_address)
            save_frame = model.initilize_model(frame_no)
            msg = 'Four:',len(save_frame[0]),'Out:',len(save_frame[1])
            # print('Info calling befor')
            # info_window('Info',msg)
            print(save_frame,"checkbox",video_address)
            clip.cutclip(save_frame, check_box, video_address)
            if check_box[2] and not check_box[1]:  # if checkbox out is checked
                clip.merge_videos(save_frame[1])
            elif check_box[1] and not check_box[2]:  # if checkbox four is checked
                clip.merge_videos(save_frame[0])
            else:
                clip.merge_videos(save_frame[3])
            info_window('Message','Output Saved Parent Folder')
    else:
        info_window('Alert', 'Please Select Option First!')


def info_window(title, msg):
    root = Tk()
    root.geometry("400x100")
    root.config(background='white')
    root.title(title)
    root.minsize(400, 100)
    root.maxsize(400, 100)
    # Label(root, text='Alert',foreground='red', background='white', font=('times',30,'bold')).pack(pady=10)
    Message(root, width=400, text=msg, background='white', font=('roboto', 18, 'bold'), pady=20).place(x=18, y=20)
    root.mainloop()
    time.sleep(5)
    root.destroy()

