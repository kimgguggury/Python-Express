import numpy as np

a = np.linspace(0,9,10)
a[5:9] = -1 * a[5:9]
print(a)