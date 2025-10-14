import numpy as np
import matplotlib.pyplot as plt

'''
stars = np.loadtxt('stars.csv', dtype = np.float64, delimiter=',')
check = np.loadtxt('check.csv', dtype = int, delimiter=',')
index = np.loadtxt('index.csv', dtype = int, delimiter=',')

check_bool = np.array(check/5, dtype=bool)
print(len(stars))
mu = np.mean(stars[check_bool])
sd = np.std(stars[check_bool])

print(np.unique(stars[check_bool], return_counts=True))

plt.hist(stars[check_bool], bins = np.unique(stars[check_bool], return_counts=False))
plt.show()
'''

big_array = np.zeros(10000000000000000)

def counter