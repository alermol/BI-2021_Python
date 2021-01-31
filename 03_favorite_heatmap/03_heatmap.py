import numpy as np
import matplotlib.pyplot as plt


np.random.seed(5671)


array = np.random.random((300, 300))
plt.imshow(array, cmap='Greys_r')
plt.title('Favorite plot - heatmap of white noise')
plt.show()
