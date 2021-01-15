import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(5671)

POINT_NUMBER = 50

# generate random dataframe
df = pd.DataFrame(np.random.randint(low=0,
                                    high=101,
                                    size=(POINT_NUMBER, 2)),
                  columns=list('XY'))
df.sort_values('X', inplace=True)
df.drop_duplicates('X', inplace=True)

plt.plot(df['X'], df['Y'], c='green')
plt.title('Lineplot for random data')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.savefig('01_random_lineplot.jpeg', bbox_inches='tight')
