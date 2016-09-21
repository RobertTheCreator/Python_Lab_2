import numpy as np
x = int(input())
a = np.log(np.exp((np.sin(x)+1)**(-1))) - np.log(1.25+x**(-0.2))
b = np.log(1 + x**2)
y = a/b
print(y)