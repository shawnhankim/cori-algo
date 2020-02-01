
"""
number     depth
1          1
2          2
3          2
4          3
5          3
6          3
7          3

1    2**0
2-3  2**1 
4-7  2**2
8-15 2**3

"""

from math import log

def get_depth(val):
    share = int(log(val, 2))
    return share

stk = []
for i in range(1, 10):
    depth = get_depth(i)
    print(f"{i}. depth : {depth}")
