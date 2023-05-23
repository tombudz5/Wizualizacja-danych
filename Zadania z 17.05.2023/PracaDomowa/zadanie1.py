import matplotlib.pyplot as mpl
import numpy as np

x = np.arange(1, 21)
y = 1/x

mpl.plot(x, y, 'r-', label="Funkcja liniowa")
mpl.axis([1, 21, 0, 1])
mpl.xlabel('x')
mpl.ylabel('f(x)')
mpl.legend()
mpl.show()

