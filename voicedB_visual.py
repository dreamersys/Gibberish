import os
import time
import struct
import pyaudio
import threading
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as maxminline
from collections import OrderedDict


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

class voice_input():

    def __init__(self):
        self.CHUNK = 1024 * 4
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.p = pyaudio.PyAudio()
        self.Amplot = OrderedDict([(0, 0)])
        self.IsRecording = False
        self.IsPause = False
        self.t_pause = 0
        self.loud_score = 0

    def set_pause(self):
        self.t_pause = time.clock()
        print(self.t_pause)
        self.IsPause = True

    def set_resume(self):
        self.IsPause = False

    def set_IsRecording(self):
        self.IsRecording = False

    def print_amp_stat(self):
        last_key = self.Amplot.popitem()[0]
        #print(last_key)
        fig, ax = plt.subplots()

        ax.set_ylim(-150, 150)
        ax.set_xlim(0, last_key)

        dB_max1 = maxminline.Line2D([0, last_key], [100, 100])
        dB_max2 = maxminline.Line2D([0, last_key], [-100, -100])
        dB_min1 = maxminline.Line2D([0, last_key], [10, 10])
        dB_min2 = maxminline.Line2D([0, last_key], [-10, -10])

        dB_max1.set_color("#ffc0c0")
        dB_max2.set_color("#ffc0c0")
        dB_min1.set_color("#c0f1ff")
        dB_min2.set_color("#c0f1ff")

        plt.legend([dB_max1, dB_min1], ["Max dB", "Min dB"], loc='lower right')

        ax.add_line(dB_max1)
        ax.add_line(dB_max2)
        ax.add_line(dB_min1)
        ax.add_line(dB_min2)

        plt.plot(*zip(*sorted(self.Amplot.items())))

        plt.show()
        #filename = input("Please enter the file name.")

        amp_stat_image_path = os.path.join(os.getcwd(), 'Source_Image/')
        fig.savefig(amp_stat_image_path + 'Gibberish_stats' + '.png')
        plt.close()
        self.get_loudness_score()
        return 0

    def capture_voice(self):

        self.IsRecording = True
        # initialize a audio stream
        stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK
        )

        v_in = voice_input()

        stream = v_in.capture_voice()
        v_in.IsRecording = True
        fig, ax = plt.subplots()
        x = np.arange(0, 2 * v_in.CHUNK, 2)
        line, = ax.plot(x, np.random.rand(v_in.CHUNK))

        # set x/y axis limit
        ax.set_ylim(-150, 150)
        ax.set_xlim(0, v_in.CHUNK)

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
                # print(v_in.Amplot)

                # update the graph instantly and refresh
                line.set_ydata(data_int)
                fig.canvas.draw()
                fig.show()
                fig.canvas.flush_events()
            # print the stat page

    def get_loudness_score(self):
        for value in self.Amplot.values():
            if (value > 100 or value < 10):
                self.loud_score+=1
        print(self.loud_score)
