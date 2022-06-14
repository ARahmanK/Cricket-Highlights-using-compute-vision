from moviepy.editor import *


class ClipCutting:
    def cutclip(self, save_frame,check_box,path):
        complete_video = VideoFileClip(path)
        print("save frame: ",save_frame,"\n checkBox",check_box,"\n",path)

        # clipping of the video
        if check_box[2]:# checkbox out is checked
            for rec in save_frame[1]:
                event_sec = int(rec) / 2
                clip = complete_video.subclip(int(event_sec)-15, int(event_sec) + 15)
                clip.write_videofile(rec + '.mp4')
        if check_box[1]: # if checkbox four is checked
            for rec in save_frame[0]:
                event_sec = int(rec) / 2
                clip = complete_video.subclip(int(event_sec) - 15, int(event_sec) + 15)
                clip.write_videofile(rec + '.mp4')
        # for rec in save_frame[2]: #six is checked
        #     event_sec = int(rec) / 2
        #     clip = complete_video.subclip(int(event_sec) - 15, int(event_sec) + 15)
        #     clip.write_videofile(rec + '.mp4')

    def merge_videos(self, clip_names):
        clip_lst = []
        clips = ['/home/ark/FYP1/' + rec + '.mp4' for rec in clip_names]
        for rec in clips:
            clip = VideoFileClip(rec)
            clip_lst.append(clip)

        final = concatenate_videoclips(clip_lst)
        # showing final clip
        # final.ipython_display(width=480)
        # writing the video into a file / saving the combined video
        final.write_videofile("Highlights.mp4", codec="libx264")
