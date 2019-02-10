from tkinter import *
from tkinter import font
import cv2
import time
import PIL
from PIL import Image, ImageTk
from Object_detection_webcam import arm_detect

WIDTH = 640 * 2
HEIGHT = 533.33 * 2
prev_time = 0
prev_avg_cood = [0, 0]
video = cv2.VideoCapture(0)
root = Tk()
root.title("Gibberish")
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
logo_image = PhotoImage(file="./Source_Image/GibberishLogo.png")


def intro():
    def open_help():
        def show_help_buttons():
            about_button.place(rely=0.1, relx=0.85, relwidth=0.1, relheight=0.05)
            tutorial_button.place(rely=0.2, relx=0.85, relwidth=0.1, relheight=0.05)
            analyze_button.place(rely=0.3, relx=0.85, relwidth=0.1, relheight=0.05)
            history_button.place(rely=0.4, relx=0.85, relwidth=0.1, relheight=0.05)
            settings_button.place(rely=0.5, relx=0.85, relwidth=0.1, relheight=0.05)
            exit_button.place(rely=0.6, relx=0.85, relwidth=0.1, relheight=0.05)

        def close_help():
            arrow_button.destroy()
            help_desk.destroy()
            about_button.place(relwidth=0, relheight=0)
            tutorial_button.place(relwidth=0, relheight=0)
            analyze_button.place(relwidth=0, relheight=0)
            history_button.place(relwidth=0, relheight=0)
            settings_button.place(relwidth=0, relheight=0)
            exit_button.place(relwidth=0, relheight=0)

        # arrow_image = PhotoImage(file="./Source_Image/arrow.png")
        # arrow_image = arrow_image.zoom(15)
        # arrow_image = arrow_image.subsample(30)
        arrow_button = Button(root, image=help_image, relief=SUNKEN, command=close_help)
        arrow_button.place(relx=0.77, rely=0.05, relheight=0.027)
        help_desk = Label(root, bg="#E5E5E5")
        help_desk.place(relx=0.8, relwidth=0.2, relheight=0.9)
        about_button = Button(root, text="About")
        tutorial_button = Button(root, text="Tutorial")
        analyze_button = Button(root, text="Analyze")
        history_button = Button(root, text="History")
        settings_button = Button(root, text="Settings")
        exit_button = Button(root, text="Exit")
        show_help_buttons()

    frame = Frame(root, bd=10)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.65, anchor="n")
    lower_frame = Frame(root, bd=5)
    lower_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=0.5, anchor="n")

    logo_label = Label(frame, image=logo_image)
    logo_label.place(relwidth=1, relheight=1)
    help_image = PhotoImage(file="./Source_Image/3lines.png")
    help_image = help_image.zoom(15)
    help_image = help_image.subsample(30)
    help_button = Button(root, image=help_image, relief=SUNKEN, command=open_help)
    help_button.place(relx=0.92, rely=0.05, relheight=0.027)

    startButton = Button(lower_frame, text="Start", relief=SUNKEN, bg="#A2A2A2", command=lambda: (chapter2()),
                         font=("Source Serif Variable", 20))
    startButton.place(relx=0.40, rely=0.4, relwidth=0.2, relheight=0.2)

    caption = Label(lower_frame, text="A software that makes us better speakers", font=("Source Serif Variable", 20))
    caption.place(rely=-0.05, relx=0.5, relwidth=0.8, relheight=0.15, anchor="n")
    version_label = Label(lower_frame, text="V1.0.0", font=("Source Serif Variable", 11))
    version_label.place(relx=0.05, rely=0.90)
    team_name_label = Label(lower_frame, text="A product of D_Major", font=("Source Serif Variable", 11))
    team_name_label.place(relx=0.85, rely=0.90)


pause_image = PhotoImage(file="./Source_Image/pause.png")
stop_image = PhotoImage(file="./Source_Image/stop.png")
screenshot_image = PhotoImage(file="./Source_Image/screenshot.png")


def chapter2():
    def show_frame():
        global prev_time, prev_avg_cood
        _, frame = video.read()
        height, width = frame.shape[:2]
        frame = cv2.resize(frame, (0, 0), fx=WIDTH / width, fy=HEIGHT / height)
        frame = cv2.flip(frame, 1)
        # print(prev_avg_cood)
        img, prev_time, prev_avg_cood = arm_detect(frame, prev_time, prev_avg_cood)
        # print(prev_avg_cood)
        cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)

    frame = Frame(root, bg="#80c1ff", bd=5)
    frame.place(relx=0.5, rely=0, relwidth=1, relheight=0.9, anchor="n")

    lmain = Label(frame)
    lmain.pack()

    lower_frame = Frame(root, bd=10)
    lower_frame.place(relx=0.5, rely=0.9, relwidth=1, relheight=0.1, anchor="n")

    start_button = Button(lower_frame, image=pause_image, relief="flat", borderwidth=0)
    start_button.place(relx=0.05, rely=0, relheight=1)

    # pause_image = PhotoImage(file="./Source_Image/pause.png")
    pause_button = Button(lower_frame, image=pause_image, relief="flat", borderwidth=0)
    pause_button.place(relx=0.1, rely=0, relheight=1)

    resume_button = Button(lower_frame, image=pause_image, relief="flat", borderwidth=0)
    resume_button.place(relx=0.15, rely=0, relheight=1)

    # stop_image = PhotoImage(file="./Source_Image/stop.png")
    stop_button = Button(lower_frame, image=stop_image, relief="flat",
                         command=lambda: (root.destroy(),chapter3()))
    stop_button.place(relx=0.2, rely=0, relheight=1)

    # screenshot_image = PhotoImage(file="./Source_Image/screenshot.png")
    screenshot_button = Button(lower_frame, image=screenshot_image, relief="flat")
    screenshot_button.place(relx=0.9, rely=0, relheight=1)

    wave_label = Label(lower_frame, text="HI THERE", bg="#ffffff")
    wave_label.place(relx=0.5, rely=0.25)

    show_frame()


def chapter3():
    class StatFrame(Tk):

        def __init__(self, *args, **kwargs):
            Tk.__init__(self, *args, **kwargs)

            self.title_font = font.Font(family='Helvetica', size=18, weight="bold", slant="italic")
            self.title("Gibberish")
            # the container is where we'll stack a bunch of frames
            # on top of each other, then the one we want visible
            # will be raised above the others
            container = Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}
            for F in (PageOne, PageTwo, PageThree, PageFour):
                page_name = F.__name__
                frame = F(parent=container, controller=self)
                self.frames[page_name] = frame

                # put all of the pages in the same location;
                # the one on the top of the stacking order
                # will be the one that is visible.
                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame("PageOne")

        def show_frame(self, page_name):
            '''Show a frame for the given page name'''
            frame = self.frames[page_name]
            frame.tkraise()

    class PageOne(Frame):

        def __init__(self, parent, controller):
            def button_tab():
                button1 = Button(self, text="Overall", font=("Source Serif Variable",20),
                                 command=lambda: controller.show_frame("PageOne"))
                button2 = Button(self, text="Loudness",font=("Source Serif Variable",11),
                                 command=lambda: controller.show_frame("PageTwo"))
                button3 = Button(self, text="Movement",font=("Source Serif Variable",11),
                                 command=lambda: controller.show_frame("PageThree"))
                button4 = Button(self, text="Speech",font=("Source Serif Variable",11),
                                 command=lambda: controller.show_frame("PageFour"))
                button1.place(rely=0.88, relx=0, relwidth=0.25, relheight=0.12)
                button2.place(rely=0.9, relx=0.25, relwidth=0.25, relheight=0.1)
                button3.place(rely=0.9, relx=0.5, relwidth=0.25, relheight=0.1)
                button4.place(rely=0.9, relx=0.75, relwidth=0.25, relheight=0.1)

            Frame.__init__(self, parent)
            canvas = Canvas(self, height=400 * 2, width=640 * 2)
            canvas.pack()
            self.controller = controller
            label = Label(self, text="69", font=("Source Serif Variable",150), fg="#FF0000")
            label.place(relx=0.5, rely=0.4, anchor="n")
            button_tab()

    class PageTwo(Frame):

        def __init__(self, parent, controller):
            def button_tab():
                button1 = Button(self, text="Overall",font=("Source Serif Variable",11),
                                 command=lambda: controller.show_frame("PageOne"))
                button2 = Button(self, text="Loudness",font=("Source Serif Variable",20),
                                 command=lambda: controller.show_frame("PageTwo"))
                button3 = Button(self, text="Movement",font=("Source Serif Variable",11),
                                 command=lambda: controller.show_frame("PageThree"))
                button4 = Button(self, text="Speech",font=("Source Serif Variable",11),
                                 command=lambda: controller.show_frame("PageFour"))
                button1.place(rely=0.9, relx=0, relwidth=0.25, relheight=0.1)
                button2.place(rely=0.88, relx=0.25, relwidth=0.25, relheight=0.12)
                button3.place(rely=0.9, relx=0.5, relwidth=0.25, relheight=0.1)
                button4.place(rely=0.9, relx=0.75, relwidth=0.25, relheight=0.1)

            Frame.__init__(self, parent)
            self.controller = controller
            label = Label(self, text="This is Loudness Page", font=controller.title_font)
            label.place(relx=0.5, rely=0.5, anchor="n")
            button_tab()

    class PageThree(Frame):

        def __init__(self, parent, controller):
            def button_tab():
                button1 = Button(self, text="Overall",font=("Source Serif Variable",11),
                                 command=lambda: controller.show_frame("PageOne"))
                button2 = Button(self, text="Loudness",font=("Source Serif Variable",11),
                                 command=lambda: controller.show_frame("PageTwo"))
                button3 = Button(self, text="Movement",font=("Source Serif Variable",20),
                                 command=lambda: controller.show_frame("PageThree"))
                button4 = Button(self, text="Speech",font=("Source Serif Variable",11),
                                 command=lambda: controller.show_frame("PageFour"))
                button1.place(rely=0.9, relx=0, relwidth=0.25, relheight=0.1)
                button2.place(rely=0.9, relx=0.25, relwidth=0.25, relheight=0.1)
                button3.place(rely=0.88, relx=0.5, relwidth=0.25, relheight=0.12)
                button4.place(rely=0.9, relx=0.75, relwidth=0.25, relheight=0.1)

            Frame.__init__(self, parent)
            self.controller = controller
            label = Label(self, text="This is Movement Page", font=controller.title_font)
            label.place(relx=0.5, rely=0.5, anchor="n")
            button_tab()

    class PageFour(Frame):

        def __init__(self, parent, controller):
            def button_tab():
                button1 = Button(self, text="Overall",font=("Source Serif Variable",11),
                                 command=lambda: controller.show_frame("PageOne"))
                button2 = Button(self, text="Loudness",font=("Source Serif Variable",11),
                                 command=lambda: controller.show_frame("PageTwo"))
                button3 = Button(self, text="Movement",font=("Source Serif Variable",11),
                                 command=lambda: controller.show_frame("PageThree"))
                button4 = Button(self, text="Speech",font=("Source Serif Variable",20),
                                 command=lambda: controller.show_frame("PageFour"))
                button1.place(rely=0.9, relx=0, relwidth=0.25, relheight=0.1)
                button2.place(rely=0.9, relx=0.25, relwidth=0.25, relheight=0.1)
                button3.place(rely=0.9, relx=0.5, relwidth=0.25, relheight=0.1)
                button4.place(rely=0.88, relx=0.75, relwidth=0.25, relheight=0.12)
            Frame.__init__(self, parent)
            self.controller = controller
            titleLabel = Label(self, text="Speech to Text", font=("Source Serif Variable",25))
            titleLabel.place(relx=0.5, rely=0.3, anchor="n")
            with open("./Text.txt", "r") as f:
                Label(self, text=f.read(), wraplength=500).place(relx=0.5, rely=0.4, anchor="n")
            repeatedLabel = Label(self, text="Number of repeated words :", font=("Source Serif Variable",25))
            repeatedLabel.place(relx=0.45, rely=0.8, anchor="n")
            with open("./Repeated.txt", "r") as f:
                Label(self, text=f.read(), font=("Source Serif Variable",25),wraplength=500).place(relx=0.6, rely=0.8,anchor="n")
            button_tab()

    if __name__ == "__main__":
        app = StatFrame()
        app.mainloop()


intro()

root.mainloop()
