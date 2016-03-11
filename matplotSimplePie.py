import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt

values = [3, 5, 10, 30, 2, 40, 9, 1]
cs = cm.Set1(np.arange(len(values)) / 10.)
plt.pie(values, colors=cs)
plt.show()
