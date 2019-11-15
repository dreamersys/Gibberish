from tkinter import *

root = Tk()
root.title("Image Loader")
root.minsize(300,300)
w = 800  # width for the Tk root
h = 650  # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

btn = Button(root, text="Select an image", command=None)
btn.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

root.mainloop()
