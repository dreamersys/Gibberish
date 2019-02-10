from tkinter import *

root = Tk()
root.title("Gibberish")

canvas = Canvas(root, height=720, width=1280)
canvas.pack()

frame = Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0, relwidth = 1, relheight=0.9, anchor="n")

lower_frame = Frame(root, bd=10)
lower_frame.place(relx=0.5, rely=0.9,relwidth = 1,relheight = 0.1, anchor="n")

pause_image=PhotoImage(file="./Source_Image/pause.png")
pause_button=Button(lower_frame,image=pause_image, relief=SUNKEN, bg="#B3B3B3", borderwidth=0)
pause_button.place(relx=0.05,rely=0, relheight=1)

stop_image=PhotoImage(file="./Source_Image/stop.png")
stop_button=Button(lower_frame,image=stop_image, relief=SUNKEN, bg="#B3B3B3")
stop_button.place(relx=0.1,rely=0, relheight=1)

screenshot_image=PhotoImage(file="./Source_Image/screenshot.png")
screenshot_button=Button(lower_frame,image=screenshot_image, relief=SUNKEN, bg="#B3B3B3")
screenshot_button.place(relx=0.9,rely=0, relheight=1)

root.mainloop()

