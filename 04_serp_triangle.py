import matplotlib.pyplot as plt
import numpy as np

np.random.seed(5671)

POINTS_NUMBER = 100000

apexes = {
    0: np.array([0, 1]),
    1: np.array([-1, -1]),
    2: np.array([1, -1])
}

for a in apexes.values():
    plt.scatter(a[0], a[1], marker='.', c='green', s=0.1)

points = np.zeros((POINTS_NUMBER, 2))
apex = np.random.randint(low=0, high=3, size=POINTS_NUMBER)
points[0] = np.random.uniform(low=-1, high=1, size=2)
for i in range(1, POINTS_NUMBER):
    points[i][0] = 0.5 * (points[i - 1][0] + apexes[apex[i]][0])
    points[i][1] = 0.5 * (points[i - 1][1] + apexes[apex[i]][1])
points = np.transpose(points)
plt.scatter(points[0], points[1], marker='.', c='green', s=0.1)
plt.axis('off')
plt.show()
