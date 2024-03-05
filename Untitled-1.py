import matplotlib.pyplot as plt
import numpy as np
number = [2,255,127,64, 32, 5, 0]
voltage = [0.0728,3.244,1.676, 0.886, 0.456, 0.1118, 0.0471]
z = np.poly1d(np.polyfit(number, voltage, deg = 1))
fig, ax = plt.subplots(figsize = (16,9))
ax.errorbar(number, voltage, marker = 'o', markersize = 7)
ax.plot(number, z(number))
ax.grid()
plt.show()

