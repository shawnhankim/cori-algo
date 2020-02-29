"""
Power Set

Expected Results:

1. test_case : ['a', 'b', 'c']
    - power set count : 8
    -           data  : [['a', 'b', 'c'], ['a', 'b'], ['a', 'c'], ['a'], ['b', 'c'], ['b'], ['c'], []]
2. test_case : ['a', 'b', 'c', 'd']
    - power set count : 16
    -           data  : [['a', 'b', 'c', 'd'], ['a', 'b', 'c'], ['a', 'b', 'd'], ['a', 'b'], ['a', 'c', 'd'], ['a', 'c'], ['a', 'd'], ['a'], ['b', 'c', 'd'], ['b', 'c'], ['b', 'd'], ['b'], ['c', 'd'], ['c'], ['d'], []]
3. test_case : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    - power set count : 1024

"""

import copy

def power_set(l1):
    res, s = [], []
    return helper(l1, res, s, k=0, n=len(l1))


def helper(l1, res, s, k, n):
    if k > n: return res
    if k == n:
        res.append(copy.deepcopy(s))
        return res
    s.append(l1[k])
    res = helper(l1, res, s, k+1, n)
    s.pop()
    return helper(l1, res, s, k+1, n)


def test():
    test_cases = [
        ['a', 'b', 'c'],
        ['a', 'b', 'c', 'd'],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    for i, l1 in enumerate(test_cases, 1):
        res = power_set(l1)
        print(f"{i}. test_case : {l1}")
        print(f"    - power set count : {len(res)}")
        print(f"    -           data  : {res}") 

if __name__ == '__main__':
    test()

