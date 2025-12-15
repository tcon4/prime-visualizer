# import matplotlib.pyplot as plt
# ... all your other code ...

# COMMENT OUT OR REMOVE animate_sieve(100)

# TEST CODE:
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    return ln,

def update(frame):
    print(f"Frame {frame}")
    xdata.append(frame)
    ydata.append(frame)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=range(10), init_func=init, interval=500, repeat=False)
plt.show()