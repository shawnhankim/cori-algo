"""

Min Heap Sort

Expected Results:

1. Test Case : []
   - Result of heap_min_sort()         : []
   - Result of sorted()                : []
   - Assert heap_min_sort() == sorted(): True

2. Test Case : [2]
   - Result of heap_min_sort()         : [2]
   - Result of sorted()                : [2]
   - Assert heap_min_sort() == sorted(): True

3. Test Case : [3, 2]
   - Result of heap_min_sort()         : [2, 3]
   - Result of sorted()                : [2, 3]
   - Assert heap_min_sort() == sorted(): True

4. Test Case : [2, 3, 1]
   - Result of heap_min_sort()         : [1, 2, 3]
   - Result of sorted()                : [1, 2, 3]
   - Assert heap_min_sort() == sorted(): True

5. Test Case : [2, 2, 4, 3, 3, 5, 1]
   - Result of heap_min_sort()         : [1, 2, 2, 3, 3, 4, 5]
   - Result of sorted()                : [1, 2, 2, 3, 3, 4, 5]
   - Assert heap_min_sort() == sorted(): True

6. Test Case : [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
   - Result of heap_min_sort()         : [0, 1, 2, 2, 3, 3, 5, 5, 6, 6, 8]
   - Result of sorted()                : [0, 1, 2, 2, 3, 3, 5, 5, 6, 6, 8]
   - Assert heap_min_sort() == sorted(): True

"""

import copy
import heapq

def heap_min_sort(l1):
    h = []
    for v in l1:
        heapq.heappush(h, v)
    res = [heapq.heappop(h) for i in range(len(l1))]
    return res
    

def test_heap_min_sort():
    test_cases = [
        [],
        [2],
        [3, 2],
        [2, 3, 1],
        [2, 2, 4, 3, 3, 5, 1],
        [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    ]
    for i, l1 in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : {l1}")
        res1 = heap_min_sort(copy.deepcopy(l1))
        res2 = sorted(l1)

        print(f"   - Result of heap_min_sort()         : {res1}")
        print(f"   - Result of sorted()                : {res2}")
        print(f"   - Assert heap_min_sort() == sorted(): {res1 == res2}")


if __name__ == '__main__':
    test_heap_min_sort()

