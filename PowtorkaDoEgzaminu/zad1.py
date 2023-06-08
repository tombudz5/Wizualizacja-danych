import matplotlib.pyplot as plt

data1 = [15.7, 25.58, 16.86, 21.51, 12.79, 7.56]
data2 = [20.37, 17.59, 9.72, 19.91, 15.74, 16.67]
data_labels = ['A', 'B', 'C', 'D', 'E', 'F']
colors = ['sienna', 'orchid', 'tan', 'lime', 'sienna', 'dodgerblue']
explode = (0, 0.1, 0, 0, 0, 0)
fig, axs = plt.subplots(2, 2, figsize=(6,6))
axs[0,0].pie(data1, labels=data_labels, autopct='%.2f%%', colors=colors, startangle=45, explode=explode)
axs[0,0].set_title("Lewo Góra")
axs[1,1].pie(data2, labels=data_labels, autopct='%.2f%%', colors=colors, startangle=45, explode=explode)
axs[1,1].set_title("Prawo Dół")
fig.delaxes(axs[0, 1])
fig.delaxes(axs[1, 0])
plt.savefig('zad1.jpg')
plt.show()
