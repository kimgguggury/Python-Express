import numpy as np

heights = np.array([ 1.83, 1.76, 1.69, 1.86, 1.77, 1.73 ])
weights = np.array([ 86,     74,  59,   95,    80,   68 ])

BMI = weights/(heights**2)
print(BMI)