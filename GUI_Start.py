from tkinter import *


root = Tk()

canvas = Canvas(root, height=720, width=1280)
canvas.pack()

frame = Frame(root, bd=10)
frame.place(relx=0.5, rely=0.1, relwidth = 0.75, relheight=0.5, anchor="n")

logo_image= PhotoImage(file="./GibberishLogo.png")
logo_image= logo_image.zoom(25)
logo_image= logo_image.subsample(30)
logo_label=Label(frame,image=logo_image)
logo_label.place(relwidth=1,relheight=1)

caption= Label(frame, text="A software that makes us better speakers")
caption.place(relwidth=0.8,relheight=0.1)

lower_frame = Frame(root, bd=5)
lower_frame.place(relx=0.5, rely=0.5,relwidth = 0.75,relheight = 0.4, anchor="n")

startButton = Button(lower_frame, text="Start", font=40, bg="#C0C0C0")
startButton.place(relx=0.333, rely=0.8, relwidth=0.3,relheight=0.2)

root.mainloop()