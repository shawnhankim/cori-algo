"""

Merge Sort with Popping List : O(n Log n)

Expect Results:

1. Test Case : []
   - Result of merge_sort_pop() : []
   - Result of sorted()         : []
   - Assert merge_sort_pop() == sorted() : True

2. Test Case : [-9]
   - Result of merge_sort_pop() : [-9]
   - Result of sorted()         : [-9]
   - Assert merge_sort_pop() == sorted() : True

3. Test Case : [5, -3]
    * depth 0. [5] + [-3] -> [-3, 5]
   - Result of merge_sort_pop() : [-3, 5]
   - Result of sorted()         : [-3, 5]
   - Assert merge_sort_pop() == sorted() : True

4. Test Case : [inf, -inf]
    * depth 0. [inf] + [-inf] -> [-inf, inf]
   - Result of merge_sort_pop() : [-inf, inf]
   - Result of sorted()         : [-inf, inf]
   - Assert merge_sort_pop() == sorted() : True

5. Test Case : [9223372036854775807, -9223372036854775808]
    * depth 0. [9223372036854775807] + [-9223372036854775808] -> [-9223372036854775808, 9223372036854775807]
   - Result of merge_sort_pop() : [-9223372036854775808, 9223372036854775807]
   - Result of sorted()         : [-9223372036854775808, 9223372036854775807]
   - Assert merge_sort_pop() == sorted() : True

6. Test Case : [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    * depth 2. [3] + [5] -> [3, 5]
    * depth 3. [6] + [8] -> [6, 8]
    * depth 2. [2] + [6, 8] -> [2, 6, 8]
    * depth 1. [3, 5] + [2, 6, 8] -> [2, 3, 5, 6, 8]
    * depth 3. [0] + [3] -> [0, 3]
    * depth 2. [1] + [0, 3] -> [0, 1, 3]
    * depth 3. [6] + [2] -> [2, 6]
    * depth 2. [5] + [2, 6] -> [2, 5, 6]
    * depth 1. [0, 1, 3] + [2, 5, 6] -> [0, 1, 2, 3, 5, 6]
    * depth 0. [2, 3, 5, 6, 8] + [0, 1, 2, 3, 5, 6] -> [0, 1, 2, 2, 3, 3, 5, 5, 6, 6, 8]
   - Result of merge_sort_pop() : [0, 1, 2, 2, 3, 3, 5, 5, 6, 6, 8]
   - Result of sorted()         : [0, 1, 2, 2, 3, 3, 5, 5, 6, 6, 8]
   - Assert merge_sort_pop() == sorted() : True

7. Test Case : [9, 9, 8, 7, 1, 2, 2, 5, 2, 3, 3, 2]
    * depth 3. [9] + [8] -> [8, 9]
    * depth 2. [9] + [8, 9] -> [8, 9, 9]
    * depth 3. [1] + [2] -> [1, 2]
    * depth 2. [7] + [1, 2] -> [1, 2, 7]
    * depth 1. [8, 9, 9] + [1, 2, 7] -> [1, 2, 7, 8, 9, 9]
    * depth 3. [5] + [2] -> [2, 5]
    * depth 2. [2] + [2, 5] -> [2, 2, 5]
    * depth 3. [3] + [2] -> [2, 3]
    * depth 2. [3] + [2, 3] -> [2, 3, 3]
    * depth 1. [2, 2, 5] + [2, 3, 3] -> [2, 2, 2, 3, 3, 5]
    * depth 0. [1, 2, 7, 8, 9, 9] + [2, 2, 2, 3, 3, 5] -> [1, 2, 2, 2, 2, 3, 3, 5, 7, 8, 9, 9]
   - Result of merge_sort_pop() : [1, 2, 2, 2, 2, 3, 3, 5, 7, 8, 9, 9]
   - Result of sorted()         : [1, 2, 2, 2, 2, 3, 3, 5, 7, 8, 9, 9]
   - Assert merge_sort_pop() == sorted() : True

"""

import copy
import sys

def merge_sort_pop(l1, depth=0):
    n = len(l1)
    if n < 2: return l1

    m = n >> 1
    l = merge_sort_pop(l1[:m], depth+1)
    r = merge_sort_pop(l1[m:], depth+1)

    res = merge_lists(copy.deepcopy(l), copy.deepcopy(r))
    print(f"    * depth {depth}. {l} + {r} -> {res}")
    return res


def merge_lists(l, r):
    if not l or not r: return r or l

    res = []
    while l and r:
        if l[-1] > r[-1]: res.append(l.pop())
        else            : res.append(r.pop())

    res.reverse()
    return (l or r) + res


def test():
    test_cases = [
        [],
        [-9],
        [5, -3],
        [float('inf'), float('-inf')],
        [sys.maxsize, -sys.maxsize-1],
        [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2],
        [9, 9, 8, 7, 1, 2, 2, 5, 2, 3, 3, 2]
    ]
    for i, l1 in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : {l1}")
        res1 = merge_sort_pop(copy.deepcopy(l1))
        res2 = sorted(l1)

        print(f"   - Result of merge_sort_pop() : {res1}")
        print(f"   - Result of sorted()         : {res2}")
        print(f"   - Assert merge_sort_pop() == sorted() : {res1 == res2}")


if __name__ == '__main__':
    test()

