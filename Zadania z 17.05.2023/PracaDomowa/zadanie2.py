import matplotlib.pyplot as mpl
import numpy as np

x = np.arange(1, 21)
y = 1/x

mpl.plot(x, y, 'g>:', label="f(x) = 1/x")
mpl.axis([0, 21, 0, 1])
mpl.xlabel('x')
mpl.ylabel('f(x)')
mpl.legend()
mpl.title('Wykres funkcji f(x) dla x [1. 20]')
mpl.show()

