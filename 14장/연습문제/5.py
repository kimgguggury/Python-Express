import numpy as np

a = np.zeros((5, 5), dtype=int)
a[1::2, ::2] = 1
a[::2,1::2] = 1
print(a)