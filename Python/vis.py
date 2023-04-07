import matplotlib.pyplot as plt
import numpy as np
import sys


filename = sys.argv[1]
a = []
a = np.genfromtxt(filename, delimiter=",", filling_values=0)
print(a)

plt.imshow(a, cmap='binary', interpolation='nearest')
plt.show()
