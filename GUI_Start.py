from tkinter import *

def create_tutorial_prompt():
    tutorial_prompt = Toplevel(height=400,width=400)
    tutorial_prompt.title=""
    ask_label = Label(tutorial_prompt, text="Do you want a tutorial?",font=("Source Serif Variable",25))
    ask_label.place(relx=0.5, rely=-0.2,relwidth=1, relheight=0.8, anchor="n")
    yes_button = Button(tutorial_prompt, text="Yes")
    yes_button.place(relx=0.2, rely=0.65, relwidth = 0.25, relheight=0.1, anchor="n")
    no_button = Button(tutorial_prompt, text="No")
    no_button.place(relx=0.8, rely=0.65,relwidth = 0.25, relheight=0.1, anchor="n")
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
        about_button.place(relwidth=0,relheight=0)
        tutorial_button.place(relwidth=0,relheight=0)
        analyze_button.place(relwidth=0,relheight=0)
        history_button.place(relwidth=0,relheight=0)
        settings_button.place(relwidth=0,relheight=0)
        exit_button.place(relwidth=0,relheight=0)

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

root = Tk()
root.title("Gibberish")

canvas = Canvas(root, height=720, width=1280)
canvas.pack()

frame = Frame(root, bd=10)
frame.place(relx=0.5, rely=0.1, relwidth = 0.75, relheight=0.65, anchor="n")
lower_frame = Frame(root, bd=5)
lower_frame.place(relx=0.5, rely=0.5,relwidth = 1,relheight = 0.5, anchor="n")

logo_image= PhotoImage(file="./Source_Image/GibberishLogo.png")
logo_label=Label(frame,image=logo_image)
logo_label.place(relwidth=1,relheight=1)
help_image=PhotoImage(file="./Source_Image/3lines.png")
help_image= help_image.zoom(15)
help_image= help_image.subsample(30)
help_button=Button(root,image=help_image, relief=SUNKEN, command=open_help)
help_button.place(relx=0.92,rely=0.05, relheight=0.027)

startButton = Button(lower_frame, text="Start", relief=SUNKEN, bg="#A2A2A2", command=create_tutorial_prompt,font=("Source Serif Variable",20))
startButton.place(relx=0.40, rely=0.4, relwidth=0.2,relheight=0.2)

caption= Label(lower_frame, text="A software that makes us better speakers", font=("Source Serif Variable",20))
caption.place(rely=-0.05,relx=0.5,relwidth=0.8,relheight=0.15, anchor="n")
version_label = Label(lower_frame, text = "V1.0.0",font=("Source Serif Variable",11))
version_label.place(relx=0.05, rely=0.90)
team_name_label= Label(lower_frame, text= "A product of D_Major",font=("Source Serif Variable",11))
team_name_label.place(relx=0.85,rely=0.90)



root.mainloop()