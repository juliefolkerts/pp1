#25 employees commute by car, 
#19 employees commute by public transport, 
#32 people commute by bike, and 
#7 people commute on foot

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["car", "public transport", "bike", "foot"])
y = np.array([25, 19, 32, 7])

plt.bar(x, y)
plt.show()