import matplotlib.pyplot as mpl
import numpy as np

x = ['1', '2', '3']
y = [3, 2, 1]

mpl.plot(x, y, 'r-', label="Funkcja liniowa")
mpl.axis([1, 20, 0, 1])
mpl.xlabel('x')
mpl.ylabel('f(x)')
mpl.legend()
mpl.show()

