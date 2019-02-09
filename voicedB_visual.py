import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
#import tkinter as tk

#import matplotlib.backends.tkagg as tkagg
#from matplotlib.backends.backend_agg import FigureCanvasAgg


Chunk = 1024*4
Format = pyaudio.paInt16
Channels = 1
Rate = 44100

p = pyaudio.PyAudio()

stream = p.open(
    format=Format,
    channels = Channels,
    rate = Rate,
    input = True,
    output = True,
    frames_per_buffer = Chunk
)

fig, ax = plt.subplots()

x = np.arange(0, 2*Chunk, 2)
line, = ax.plot(x, np.random.rand(Chunk))
ax.set_ylim(0, 255)
ax.set_xlim(0, Chunk)
count = 1
while True:
    data = stream.read(Chunk)
    data_int = np.array(struct.unpack(str(2*Chunk)+'B', data), dtype='b')[::2] + 127
    line.set_ydata(data_int)
    fig.canvas.draw()
    plt.show()
    fig.canvas.flush_events()



