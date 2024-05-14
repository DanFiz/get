import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap
import matplotlib.ticker as ticker

settings = np.loadtxt('C:/Users/user/Desktop/Studies_Matirials/2 семестр/Инженерная подготовка/get/settings1.txt', dtype = float)


data=np.loadtxt('C:/Users/user/Desktop/Studies_Matirials/2 семестр/Инженерная подготовка/get/data1.txt', dtype=float) * settings[1]


data_time=np.array([i*settings[0] for i in range(data.size)])

fig, ax=plt.subplots(figsize=(16, 10), dpi=400)

ax.axis([data.min(), data_time.max()+1, data.min(), data.max()+0.2])

ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))

ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

plt.ylim(0, 3.3)
plt.xlim(0, 10)

ax.set_title("\n".join(wrap('Процесс заряда и разряда конденсатора в RC-цепочке', 60)), loc = 'center', fontsize = 20)

ax.grid(which='major', color = 'gray')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':', alpha = 0.5)

ax.set_ylabel("Напряжение, В", fontsize = 15)
ax.set_xlabel("Время, с", fontsize = 15)

markers_on = np.arange(0, data.size + 1, 20)

ax.plot(data_time, data, c='blue',markevery=markers_on, marker = 'o',  label = 'V(t)')


t1 = data_time[np.argmax(data)] - data_time[0]
t2 = data_time[-1] - t1

st1 = 'Время заряда = {0:.2f} c'.format(t1)
st2 = 'Время разряда = {0:.2f} c'.format(t2)

ax.text(7, 2.25, st1, fontsize = 15)
ax.text(7, 1.75, st2, fontsize = 15)

ax.legend(shadow = False, loc = 'upper right', fontsize = 15)

fig.savefig('C:/Users/user/Desktop/Studies_Matirials/2 семестр/Инженерная подготовка/get/graph.png')
fig.savefig('C:/Users/user/Desktop/Studies_Matirials/2 семестр/Инженерная подготовка/get/graph.svg')
