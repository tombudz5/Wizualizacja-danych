import matplotlib.pyplot as mpl
import numpy as np
import pandas as pd

df = pd.read_csv('iris.data', delimiter=',')
data = {'x': np.array(df.iloc[:, 0].values),
        'y': np.array(df.iloc[:, 1].values),
        's': np.array([abs(x-y) for x, y in zip(df.iloc[:, 0].values, df.iloc[:, 1].values)])}

color_values = np.random.rand(df.shape[0])

mpl.scatter('x', 'y', c=color_values, s='s', data=data, cmap='plasma')
mpl.show()