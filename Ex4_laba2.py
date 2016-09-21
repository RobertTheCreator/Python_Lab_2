
# coding: utf-8

# In[18]:

import math
import pylab
import numpy as np


t = np.arange (0, 2*np.pi, 0.001)
pylab.ion()
a = 0
for i in range(32):
    pylab.clf()
    pylab.plot(np.sin(t+a), np.cos(2*t))
    pylab.draw()
    pylab.pause(0.01)
    a += 1/30*np.pi
pylab.close()

