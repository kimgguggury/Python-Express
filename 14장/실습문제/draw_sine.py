import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-2 * np.pi, 2* np.pi, 100)

Y1 = np.sin(X)
Y2 = 3 * np.sin(X)

plt.plot(X,Y1, X,Y2)
plt.show()