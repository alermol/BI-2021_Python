import matplotlib.pyplot as plt
import numpy as np

np.random.seed(5671)

POINTS_NUMBER = 500000

attrs = {
    0: np.array([-1, 1]),
    1: np.array([1, 1]),
    2: np.array([1, -1]),
    3: np.array([-1, -1]),  # main apexes
    4: np.array([0, 1]),
    5: np.array([1, 0]),
    6: np.array([0, -1]),
    7: np.array([-1, 0])  # secondary apexes
}

for a in attrs.values():
    plt.scatter(a[0], a[1], marker='.', c='green', s=0.1)

points = np.zeros((POINTS_NUMBER, 2))
apex = np.random.randint(low=0, high=8, size=POINTS_NUMBER)
points[0] = np.random.uniform(low=-1, high=1, size=2)
for i in range(1, POINTS_NUMBER):
    points[i][0] = (points[i - 1][0] + (2 * attrs[apex[i]][0])) / 3
    points[i][1] = (points[i - 1][1] + (2 * attrs[apex[i]][1])) / 3
points = np.transpose(points)
plt.scatter(points[0], points[1], marker='.', c='green', s=0.1)
plt.axis('off')
plt.show()
