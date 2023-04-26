import numpy as np
import pandas as pd
# df = pd.read_csv('australian.txt', header=None, sep=' ')
# print(df)

# Series
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# s = pd.Series([10, 12, 8, 14], index=['!','@','#','$'])
# print(s)

# s = pd.Series([1.0, 2, 3, 4, 5, 6, 7], index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
# print(s)

# DataFrame
# data = {'Country': ['Poland', 'Czech Republic', 'Germany'], 'Capital': ['Warsaw', 'Prague', 'Berlin'], 'Population': ['39 500 000', '8 600 000', '83 000 000']}
#
# df = pd.DataFrame(data, index=['1', '2', '3'])
# print(df)
# print(df.dtypes)

# daty = pd.date_range('20210324', periods=5)
# # print(daty)
#
# df = pd.DataFrame(np.random.randn(5,4), index=daty, columns=list('ABCD'))
# print(df)

# df = pd.read_csv('australian.txt', header=0, sep=";",decimal=',')
# print(df)
# df.to_csv('plik.csv', index=False)



# ZADANIE 1

df = pd.read_excel('imiona.xlsx', header=None, skiprows=1)

# ZADANIE 2


# df[2] = df[2].astype(int)
# print(df[df[2] > 1000])


# print(df[df[1] == "TOMASZ"])


# sum = 0
# for child_count in df[2]:
#     sum += child_count
#
# print(sum)


sum = 0
for liczba_urodzen in df[(df[0] >= 2000) & (df[0] <= 2005)][2]:
    sum += liczba_urodzen

print(sum)


# sum_boys = 0
# sum_girls = 0
# for boy in df[df[3] == "M"][2]:
#     sum_boys += boy
# for girl in df[df[3] == "K"][2]:
#     sum_girls += girl
#
# print(sum_boys)
# print(sum_girls)


