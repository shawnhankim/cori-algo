"""
Min & Max Heap Sort

Expected Results:

1. Test Case : []
   - Result of min_heap_sort()              : []
   - Result of sorted()                     : []
   - Assert min_heap_sort == sorted()       : True
   - Result of max_heap_sort()              : []
   - Result of sorted(l1, reverse=True)     : []
   - Assert max_heap_sort == sorted(reverse): True

2. Test Case : [2, 3]
   - Result of min_heap_sort()              : [2, 3]
   - Result of sorted()                     : [2, 3]
   - Assert min_heap_sort == sorted()       : True
   - Result of max_heap_sort()              : [3, 2]
   - Result of sorted(l1, reverse=True)     : [3, 2]
   - Assert max_heap_sort == sorted(reverse): True

3. Test Case : [1, 3, 2]
   - Result of min_heap_sort()              : [1, 2, 3]
   - Result of sorted()                     : [1, 2, 3]
   - Assert min_heap_sort == sorted()       : True
   - Result of max_heap_sort()              : [3, 2, 1]
   - Result of sorted(l1, reverse=True)     : [3, 2, 1]
   - Assert max_heap_sort == sorted(reverse): True

4. Test Case : [5, 5, 7, 2, 2, 1, 3]
   - Result of min_heap_sort()              : [1, 2, 2, 3, 5, 5, 7]
   - Result of sorted()                     : [1, 2, 2, 3, 5, 5, 7]
   - Assert min_heap_sort == sorted()       : True
   - Result of max_heap_sort()              : [7, 5, 5, 3, 2, 2, 1]
   - Result of sorted(l1, reverse=True)     : [7, 5, 5, 3, 2, 2, 1]
   - Assert max_heap_sort == sorted(reverse): True

5. Test Case : [-9223372036854775808, 3, 9223372036854775807]
   - Result of min_heap_sort()              : [-9223372036854775808, 3, 9223372036854775807]
   - Result of sorted()                     : [-9223372036854775808, 3, 9223372036854775807]
   - Assert min_heap_sort == sorted()       : True
   - Result of max_heap_sort()              : [9223372036854775807, 3, -9223372036854775808]
   - Result of sorted(l1, reverse=True)     : [9223372036854775807, 3, -9223372036854775808]
   - Assert max_heap_sort == sorted(reverse): True

"""

from copy import deepcopy
from heapq import heappush, heappop
import sys

def min_heap_sort(l1):
    h = []
    for v in l1:
        heappush(h, v)
    res = [heappop(h) for i in range(len(l1))]
    return res


def max_heap_sort(l1):
    h = []
    for v in l1:
        heappush(h, -v)
    res = [-heappop(h) for i in range(len(l1))]
    return res


def test():
    test_cases = [
        [],
        [2, 3],
        [1, 3, 2],
        [5, 5, 7, 2, 2, 1, 3],
        [-sys.maxsize-1, 3, sys.maxsize]
    ]
    for i, l1 in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : {l1}")
        res11 = min_heap_sort(deepcopy(l1))
        res12 = sorted(l1)
        res21 = max_heap_sort(deepcopy(l1))
        res22 = sorted(l1, reverse=True)

        print(f"   - Result of min_heap_sort()              : {res11}")
        print(f"   - Result of sorted()                     : {res12}")
        print(f"   - Assert min_heap_sort == sorted()       : {res11 == res12}")

        print(f"   - Result of max_heap_sort()              : {res21}")
        print(f"   - Result of sorted(l1, reverse=True)     : {res22}")
        print(f"   - Assert max_heap_sort == sorted(reverse): {res21 == res22}")


if __name__ == '__main__':
    test()

