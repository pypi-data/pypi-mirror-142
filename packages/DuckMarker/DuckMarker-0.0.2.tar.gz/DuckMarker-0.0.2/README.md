# build_duck
Add a duck marker to Matplotlib.

# Example
from build_duck import get_marker

import numpy as np

import matplotlib.pyplot as plt

marker_duck = get_marker()

x = np.linspace(0,100,20)

y = 10*np.sin(x)

plt.figure(dpi=100)

plt.plot(x,y, marker=marker_duck, ms=20)

plt.show()

plt.clf()
