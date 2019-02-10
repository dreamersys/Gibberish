from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import cv2
import time

# Jkdajfka
def select_image():
    # grab a reference to the image panels
    global panelA
    image = None

    # open a file chooser dialog and allow the user to select an input
    # image
    path = tkFileDialog.askopenfilename()
    if len(path) > 0:
        image = cv2.imread(path)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

    if panelA is None:
        # the first panel will store our original image
        panelA = Label(image=image)
        panelA.image = image
        panelA.pack(side="left", padx=10, pady=10)

        # otherwise, update the image panels
    else:
        # update the pannels
        # panelA.configure(image=image)
        panelA.image = image


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

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
panelA = None


btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

root.mainloop()
