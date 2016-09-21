
# coding: utf-8

# In[78]:

import numpy as np
import matplotlib.pyplot as plt
# t - диапазон аппромаксиационного многочлена
t = np.arange (0, 11, 0.001)
# x, y - экспериментальные данные
x = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
y = [1, 1.42, 1.76, 2, 2.24, 2.5, 3, 3.02, 3.27, 3.8]
v1, p1 = np.polyfit(x, y, deg = 1, cov = True)
v2, p2 = np.polyfit(x, y, deg = 3, cov = True)
P1 = np.poly1d(v1)
P2 = np.poly1d(v2)
plt.title('Graph', style = 'italic')
plt.plot (t, P1(t), color = 'green')
plt.plot (t, P2(t), color = 'blue')
plt.plot(x, y, 'rs')
plt.xlabel('$x$', size = 15)
plt.ylabel('$y$', size = 15)
plt.axis('equal')
plt.grid(True)
plt.show()

