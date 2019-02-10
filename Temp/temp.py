from voicedB_visual import *
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import threading
import cv2
import time
import PIL
from PIL import Image, ImageTk
from Object_detection_webcam import arm_detect

def btn_start(v_in):
    threadStart = threading.Thread(target=v_in.set_start_record())
    threadStart.start()


def btn_pause(v_in):
    threadPause = threading.Thread(target=v_in.set_pause)
    threadPause.start()


def btn_resume(v_in):
    threadresume = threading.Thread(target=v_in.set_resume)
    threadresume.start()


def btn_stop(v_in):
    threadstop = threading.Thread(target=v_in.set_IsRecording)
    threadstop.start()


v_in = voice_input()

stream = v_in.capture_voice()
v_in.IsRecording = True
fig, ax = plt.subplots()
x = np.arange(0, 2 * v_in.CHUNK, 2)
line, = ax.plot(x, np.random.rand(v_in.CHUNK))

# set x/y axis limit
ax.set_ylim(-150, 150)
ax.set_xlim(0, v_in.CHUNK)


root = Tk()
root.title("Gibberish")
timer = time.clock()
video = cv2.VideoCapture(0)
WIDTH = 1280
HEIGHT = 720

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0, relwidth = 1, relheight=0.9, anchor="n")
lmain = Label(frame)
lmain.pack()

lower_frame = Frame(root, bd=10)
lower_frame.place(relx=0.5, rely=0.9,relwidth = 1,relheight = 0.1, anchor="n")

pause_image=PhotoImage(file="./Source_Image/pause.png")
pause_button=Button(lower_frame, relief=SUNKEN, bg="#B3B3B3", borderwidth=0, command=lambda: btn_start(v_in))
pause_button.place(relx=0.05,rely=0, relheight=1)

stop_image=PhotoImage(file="./Source_Image/stop.png")
stop_button=Button(lower_frame, relief=SUNKEN, bg="#B3B3B3", command=lambda: btn_stop(v_in))
stop_button.place(relx=0.1,rely=0, relheight=1)

screenshot_image=PhotoImage(file="./Source_Image/screenshot.png")
screenshot_button=Button(lower_frame, relief=SUNKEN, bg="#B3B3B3")
screenshot_button.place(relx=0.9,rely=0, relheight=1)

#wave_label = Label(lower_frame, text="HI THERE", bg="#ffffff")
#wave_label.place(relx=0.5, rely=0.25)


def show_wave(v_in):
    while v_in.IsRecording:
        if not v_in.IsPause:
            # start the timer
            t_elap = time.clock()
            t_elap -= v_in.t_pause
            # read a chunk of sample and unpack itto array
            data = stream.read(v_in.CHUNK, exception_on_overflow=False)
            data_int = np.array(struct.unpack(str(2 * v_in.CHUNK) + 'B', data), dtype='b')[::2]

            # store the instantaneous time & loudness into dictionary
            v_in.Amplot.update({t_elap: data_int[0]})
            print(v_in.Amplot)

            # update the graph instantly and refresh
            line.set_ydata(data_int)
            fig.canvas.draw()
            fig.show()
            fig.canvas.flush_events()
    # clear figure and close plot when finish recording
    #fig.clf()
    #plt.close()
    # print the stat page
    v_in.print_amp_stat()

def show_frame():
    _, frame = video.read()
    height, width = frame.shape[:2]
    frame = cv2.resize(frame, (0, 0), fx=WIDTH/width, fy=HEIGHT/height)
    cv2image = cv2.cvtColor(arm_detect(frame), cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)


show_wave(v_in)
show_frame()
root.mainloop()

