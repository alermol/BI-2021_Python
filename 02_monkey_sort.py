import random
import time

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(5671)
random.seed(5671)


def check_sort(l: list) -> bool:
    sorted = True
    if len(l) == 1 or len(l) == 0:
        return sorted
    for i in range(0, len(l) - 1):
        if l[i] <= l[i + 1]:
            continue
        else:
            return not sorted
    return sorted


def monkey_sort(l: list) -> list:
    while not check_sort(l):
        np.random.shuffle(l)


array_sizes = np.arange(start=0, stop=10, step=1, dtype=int)
ys = np.zeros(array_sizes.shape)

iteration_number = 100000

for idx, val in enumerate(array_sizes):
    array = np.random.randint(low=0, high=10, size=val)
    values = np.zeros(iteration_number)
    for j in range(iteration_number):
        start = time.time()
        monkey_sort(array)
        values[j] = time.time() - start
    ys[idx] = np.mean(values)
    plt.errorbar(idx, np.mean(values), yerr=np.var(values), capsize=3,
                 ecolor='green')
plt.scatter(array_sizes, ys, marker='.', c='green')
plt.grid()
plt.title('Bogosort time estimation')
plt.xlabel('Array size')
plt.ylabel('Time, sec')
plt.show()
