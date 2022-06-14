# Import module
from tkinter import *
from tkinter.ttk import *
import tkinter as Tkinter
import input_func,time
from PIL import ImageTk, Image

# Create object
splash_root = Tk()
#
# # Adjust size
splash_root.title('Cricket Highlights')
splash_root.geometry("700x500")
splash_root.minsize(700, 500)
splash_root.maxsize(700, 500)

# Set background image
img_open = Image.open("assets/2.jpeg")
img_resize = img_open.resize((700, 485))
img = ImageTk.PhotoImage(img_resize)

# # Create a Label Widget to display the text or Image
image_label = Label(splash_root, image=img, font=26)
image_label.pack()


def step():
    for i in range(5):
        splash_root.update_idletasks()
        pb1['value'] += 20
        time.sleep(.2)

style = Style()
style.theme_use('alt')
style.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
pb1 = Progressbar(splash_root, orient=HORIZONTAL, style="red.Horizontal.TProgressbar", length=700, mode='determinate')
pb1.pack(expand=True)
step()



# main window function
def main():
    # destroy splash window
    splash_root.destroy()
    root = Tk()
    root.geometry("800x450")
    root.title('Cricket Highlights')
    root.minsize(800, 450)
    root.maxsize(800, 450)
    # root.config(background='white')
    m_img_open = Image.open("assets/mlogo.png")
    m_img_resize = m_img_open.resize((50, 50))
    m_img = ImageTk.PhotoImage(m_img_resize)

    # # Create a Label Widget to display the text or Image
    left_div = Label(root,width=40,background='blue')
    left_div.pack(side="left",fill=Y)
    logo=Label(left_div,text="Cricket Match",background='blue',foreground='white',font=('times',34,'bold'), width=20)
    logo.place(x=15,y=300)
    logo=Label(left_div,text="Highlights",background='#FFFF00',foreground='#002060',font=('times',34,'bold'), width=9,padding=3)
    logo.place(x=15,y=350)

    upload = Label(root, text="click on Browse File to upload video",  font=('Arial', 12, 'italic'))
    upload_file = Button(root, text='Browse File', command=lambda: input_func.open_file([var1.get(),var2.get(),var3.get()]),width=10)
    sel_w = Label(root, text="Select what types of Highlights you want",  font=('Arial', 15,'bold'))
    download = Button(root, text='Download', command=lambda: input_func.open_file(), state='disabled', width=10)

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    six = Checkbutton(root, text="Six", variable=var1, onvalue=1, offvalue=0)
    four = Checkbutton(root, text="Four", variable=var2, onvalue=1, offvalue=0)
    out = Checkbutton(root, text="Out", variable=var3, onvalue=1, offvalue=0)
    print(var1.get(),"value=111",var3.get(),"value=333")

    sel_w.place(x=390, y=100)
    six.place(x=390, y=140)
    four.place(x=390, y=180)
    out.place(x=390, y=220)
    upload.place(x=390, y=260)
    upload_file.place(x=600, y=310)
    download.place(x=390, y=310)
    # root.config(padx=100, pady=100)


# main()

# Set Interval
splash_root.after(1500, main)

# Execute tkinter
mainloop()
