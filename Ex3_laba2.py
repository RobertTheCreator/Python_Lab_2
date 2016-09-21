
# coding: utf-8

# In[17]:

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-50, 50.01, 0.01)
a = np.log((x**2+1)*np.exp((-abs(x))/10))
b = np.log(1+np.tan((1+(np.sin(x))**2)**(-1)))
plt.plot(x, a/b)
plt.show()


