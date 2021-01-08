import random
import time

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(5671)
random.seed(5671)

x = np.arange(0, 100000, 10000, dtype=int)
rand_y = np.zeros(x.shape)
np_y = np.zeros(x.shape)

for idx, val in enumerate(x):
    # random estimation
    rand_start_time = time.time()
    rand_list = [random.random() for i in range(val)]
    rand_y[idx] = time.time() - rand_start_time

    # numpy estimation
    np_start_time = time.time()
    np_list = np.random.uniform(size=val)
    np_y[idx] = time.time() - np_start_time

plt.scatter(x, rand_y, label='Random', marker='.')
plt.scatter(x, np_y, label='Numpy', marker='.')
plt.legend()
plt.grid()
plt.title('Uniform distribution generation time estimation')
plt.xlabel('Distribution size')
plt.ylabel('Time, sec')
plt.show()
