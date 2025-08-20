import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
#import matplotlib.use("Agg")
xAxis = np.array([0,10])
yAxis = np.array([0,300])
plt.plot(xAxis, yAxis)
plt.show()
plt.savefig("mydata1.pdf")