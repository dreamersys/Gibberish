from tkinter import *
import cv2
import time
import PIL
from PIL import Image, ImageTk
from Object_detection_webcam import arm_detect

root = Tk()
root.title("Gibberish")
timer = time.clock()
video = cv2.VideoCapture(0)
WIDTH = 640*2
HEIGHT = 533.33*2

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


frame = Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0, relwidth = 1, relheight=0.9, anchor="n")
lmain = Label(frame)
lmain.pack()

lower_frame = Frame(root, bd=10)
lower_frame.place(relx=0.5, rely=0.9,relwidth = 1,relheight = 0.1, anchor="n")

pause_image=PhotoImage(file="./Source_Image/pause.png")
pause_button=Button(lower_frame,image=pause_image, relief="flat", borderwidth=0)
pause_button.place(relx=0.05,rely=0, relheight=1)

stop_image=PhotoImage(file="./Source_Image/stop.png")
stop_button=Button(lower_frame,image=stop_image, relief="flat")
stop_button.place(relx=0.1, rely=0, relheight=1)

screenshot_image=PhotoImage(file="./Source_Image/screenshot.png")
screenshot_button=Button(lower_frame,image=screenshot_image, relief="flat")
screenshot_button.place(relx=0.9, rely=0, relheight=1)

wave_label = Label(lower_frame, text="HI THERE", bg="#ffffff")
wave_label.place(relx=0.5, rely=0.25)


def show_frame():
    _, frame = video.read()
    height, width = frame.shape[:2]
    print(height,width)
    frame = cv2.resize(frame, (0, 0), fx=WIDTH/width, fy=HEIGHT/height)
    cv2image = cv2.cvtColor(arm_detect(frame), cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

show_frame()
root.mainloop()

