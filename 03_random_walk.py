import matplotlib.pyplot as plt
import numpy as np

np.random.seed(5671)

WALKS_NUMBER = 100000

coords = np.zeros((WALKS_NUMBER, 2), dtype=int)
possible_move = {0: np.array([-1, 0]),  # left
                 1: np.array([1, 0]),  # right
                 2: np.array([0, 1]),  # up
                 3: np.array([0, -1])}  # down
moves = np.random.randint(low=0, high=4, size=WALKS_NUMBER - 1)
for idx, val in enumerate(moves, start=1):
    coords[idx] = coords[idx - 1] + possible_move[val]
plt.plot(coords[:, 0], coords[:, 1], color="red", lw=0.1)
plt.plot(coords[:, 0], coords[:, 1], "ro", color="blue", ms=0.5)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Random walks")
plt.show()
