from tkinter import *
import Voice_to_Text
import threading

prev = None


# @file_name: file name passed in for reading as string
def count_repeated_words(file_name):
    count = 0
    with open(file_name) as f:
        while True:
            cur_line = f.readline()
            string_list = cur_line.split()
            print(string_list)
            for i in range(0, len(string_list)-1):
                if string_list[i].lower() == string_list[i+1].lower(): # case insensitive
                    count += 1
            if not cur_line:
                break
    print(count)
    f.close()
    return count



def trollol():
    print("FUCK")


def threadButtonOne():
    thread_transcribe_sp = threading.Thread(target=Voice_to_Text.transcribe_speech)
    thread_transcribe_sp.start()


def threadButtonTROLL():
    thread_trolol = threading.Thread(target=trollol)
    thread_trolol.start()


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

btn = Button(root, text="Select an image", command=threadButtonOne)
btn.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")

btn2 = Button(root, text="Ssadjflksjdf", command=threadButtonTROLL)
btn2.pack(side="bottom", fill="both", expand="no", padx="10", pady="5")

print("Count repeat word now!")
count_repeated_words("Test.txt")
print("count completed-----------")

root.mainloop()
