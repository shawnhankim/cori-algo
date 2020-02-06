"""
Test elapsed time betweeen traditional and numpy version

Expected Result:

1. trad_version : 3.7298569679260254
2. numpy_version: 0.14579105377197266
3. difference   : 3.5840659141540527

"""


import numpy as np
import time  as tm

def trad_version():
    t = tm.time()
    x = range(10000000)
    y = range(10000000)
    z = []
    for i in range(len(x)):
        z.append(x[i] + y[i])
    return tm.time() - t


def numpy_version():
    t = tm.time()
    x = np.arange(10000000)
    y = np.arange(10000000)
    z = x + y
    return tm.time() - t


def main():
    t1 = trad_version()
    t2 = numpy_version()
    t3 = t1 - t2
    print(f"1. trad_version : {t1}")
    print(f"2. numpy_version: {t2}")
    print(f"3. difference   : {t3}")


if __name__ == '__main__':
    main()

