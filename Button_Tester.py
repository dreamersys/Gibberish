import threading
from voicedB_visual import *
from tkinter import *


def btn_start(v_in):
    threadStart = threading.Thread(target=v_in.capture_voice)
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


root = Tk()
root.title("Image Loader")
root.minsize(300, 300)
w = 800  # width for the Tk root
h = 650  # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

v_in = voice_input()

btn = Button(root, text="Start", command=lambda: btn_start(v_in))
btn.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

btn2 = Button(root, text="Pause", command=lambda: btn_pause(v_in))
btn2.pack(side="bottom", fill="both", expand="no", padx="10", pady="5")

btn2 = Button(root, text="Resume", command=lambda: btn_resume(v_in))
btn2.pack(side="bottom", fill="both", expand="no", padx="10", pady="3")

btn2 = Button(root, text="Stop", command=lambda: btn_stop(v_in))
btn2.pack(side="bottom", fill="both", expand="no", padx="10", pady="0")

root.mainloop()
