import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

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
ax.set_ylim(-255, 255)
ax.set_xlim(0, Chunk)

#fig.axis.Axis.setxscale("linear", 10)

count = 1
while True:
    data = stream.read(Chunk, exception_on_overflow = False)
    data_int = np.array(struct.unpack(str(2*Chunk) + 'B', data), dtype = 'b')[::2]
    line.set_ydata(data_int)
    fig.canvas.draw()
    fig.show()
    fig.canvas.flush_events()
