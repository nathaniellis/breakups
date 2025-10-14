import numpy as np
from time import sleep



big_array = np.arange(100000, dtype=int)[::-1] + 3


example = [1,2,3,4,5,6,7]






def counter():
    for i in range(len(big_array)):

        counter = big_array[i]
        print(counter)

        sleep(1)


counter()
