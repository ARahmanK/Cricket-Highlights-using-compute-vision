import torch,time
from tkinter import *
from tkinter.ttk import *



class Model:

    def initilize_model(self, frames_no):
        model = torch.hub.load('ultralytics/yolov5', 'custom',
                               path='/home/ark/FYP/pytorch/yolov5/runs/train/exp/weights/best.pt', force_reload=True)
        four = []
        out = []
        six = []
        mix = []
        last_four = 0
        last_out = 0
        last_six = 0
        window = self.frame_window()
        for rec in range(1, frames_no[0]):  # insert i as parameter in range
            img = str(frames_no[1]) + '/Frame' + str(rec) + '.jpg'
            results = model(img)
            self.step(window[0], window[1], rec)
            #     results.show()
            for rec in results.pandas().xyxy:
                if not rec.empty:

                    if rec.name[0]=='wicket' and rec.confidence[0]> 0.80:
                        frame_no = img.split(str(frames_no[1]) + '/Frame')[1][:-4]  # [1] list index,[:-4] removing .jpg
                        if int(frame_no) - last_out > 50:
                            print('OOHH! OUT', frame_no)
                            last_out = int(frame_no)
                            out.append(frame_no)
                            mix.append(frame_no)
                    if rec.name[0]=='four' and rec.confidence[0]>0.9:
                        frame_no = img.split(str(frames_no[1]) + '/Frame')[1][:-4]  # [1] list index,[:-4] removing .jpg
                        if int(frame_no) - last_four > 50:
                            print('Hurrah! FOUR ', frame_no)
                            last_four = int(frame_no)
                            four.append(frame_no)
                            mix.append(frame_no)
                    if rec.name[0]=='six' and rec.confidence[0]>0.90:
                        if int(frame_no) - last_six > 50:
                            print('BigOne! SIX ', frame_no)
                            last_six = int(frame_no)
                        #                 six.append(frame_no)
                        #                 mix.append(frame_no)
        return [four, out, six, mix]


    def frame_window(self):
        frames_root = Tk()
        # Adjust size
        frames_root.title('Detecting Frames')
        frames_root.geometry("400x150")
        frames_root.minsize(400, 150)
        frames_root.maxsize(400, 150)
        frames_root.config(bg="white")

        text = Label(frames_root, text="Detecting Frames", font=('times', 15), background='white')
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
        time.sleep(.0001)
        if frame == '2880':
            frames_root.destroy()