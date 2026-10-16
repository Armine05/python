import matplotlib.pyplot as plt
import numpy as np

x_axis=np.arange(1,11)
y_axis=x_axis**3
plt.plot(x_axis,y_axis)

plt.plot(x_axis,y_axis,marker='H')
plt.title('Cube function line Plort')
plt.xlabel('X axis-Value -----')
plt.ylabel('Cube of Y axis-Value --- ')


plt.show()

