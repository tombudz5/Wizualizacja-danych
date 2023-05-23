import math
import matplotlib.pyplot as mpl
import numpy as np

x = np.arange(0, 31, 0.1)
y1 = [math.sin(i) for i in x]
y2 = [math.cos(i) for i in x]

mpl.plot(x, y1, 'r-', label='sin(x)')
mpl.plot(x, y2, 'b-', label='cos(x)')
mpl.legend()
mpl.show()