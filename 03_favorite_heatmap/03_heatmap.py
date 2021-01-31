import numpy as np
import matplotlib.pyplot as plt


np.random.seed(5671)


array = np.random.random((500, 500))
plt.imshow(array, cmap='Greys_r')
plt.title('Favorite plot - heatmap of white noise')
plt.savefig('03_favorite_heatmap.jpeg', bbox_inches='tight')
