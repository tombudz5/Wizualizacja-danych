import numpy as np

liczby = np.array([1, 2, 3, 4])
# liczby2 = np.arange(15)
# liczby3 = np.arange(2, 17, dtype='int64')
# print(liczby)
# print(liczby2)
# print(liczby3)
# print(liczby3.dtype)
macierz = np.array([ [np.arange(3)],
                     [np.arange(3, 6)],
                     [np.arange(5, 11, 2)]])
print(macierz)
print(macierz.shape)
print(macierz.ndim)
print(type(macierz))

m2 = macierz.astype('float')
print(m2)
print(m2.shape)
print(m2.ndim)
print(type(m2))
