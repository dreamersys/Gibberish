import time
import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as maxminline
from collections import OrderedDict

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

    def set_pause(self):
        self.IsPause = True

    def print_amp_stat(self):
        last_key = self.Amplot.popitem()[0]
        print(last_key)
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
        filename = input("Please enter the file name.")
        fig.savefig('/Users/davidguo/Desktop/' + filename + '.png')
        plt.close()
        return 0

    def capture_voice(self):

        self.IsRecording = True
        #initialize a audio stream
        stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK
        )

        fig, ax = plt.subplots()
        x = np.arange(0, 2 * self.CHUNK, 2)
        line, = ax.plot(x, np.random.rand(self.CHUNK))

        #set x/y axis limit
        ax.set_ylim(-150, 150)
        ax.set_xlim(0, self.CHUNK)

        #start recording until the user hit stop button
        #for i in range(1, 50):
        while self.IsRecording:
            if not self.IsPause:
                #start the timer
                t_elap = time.clock()
                #read a chunk of sample and unpack itto array
                data = stream.read(self.CHUNK, exception_on_overflow=False)
                data_int = np.array(struct.unpack(str(2 * self.CHUNK) + 'B', data), dtype='b')[::2]

                #store the instantaneous time & loudness into dictionary
                self.Amplot.update({t_elap : data_int[0]})
                #print(self.Amplot)

                # update the graph instantly and refresh
                line.set_ydata(data_int)
                fig.canvas.draw()
                fig.show()
                fig.canvas.flush_events()
        #clear figure and close plot when finish recording
        fig.clf()
        plt.close()
        #print the stat page
        self.print_amp_stat()

