"""
Quick Sort with Partitioning Array

Expected Results: 

1. Test Case : []
   - Result of quick_sort()       : []
   - Result of sorted()           : []
   - Assert quick_sort == sorted(): True

2. Test Case : [2]
   - Result of quick_sort()       : [2]
   - Result of sorted()           : [2]
   - Assert quick_sort == sorted(): True

3. Test Case : [3, 2]
     * Depth:0, Left:[2]   Pivot:[3]   Right:[]
   - Result of quick_sort()       : [2, 3]
   - Result of sorted()           : [2, 3]
   - Assert quick_sort == sorted(): True

4. Test Case : [2, 3, 1]
     * Depth:0, Left:[1]   Pivot:[2]   Right:[3]
   - Result of quick_sort()       : [1, 2, 3]
   - Result of sorted()           : [1, 2, 3]
   - Assert quick_sort == sorted(): True

5. Test Case : [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
     * Depth:0, Left:[1, 2, 2, 3, 0]   Pivot:[3]   Right:[8, 6, 5, 6, 5]
     * Depth:1, Left:[0]   Pivot:[1]   Right:[2, 3, 2]
     * Depth:2, Left:[2]   Pivot:[2]   Right:[3]
     * Depth:1, Left:[5, 6, 5, 6]   Pivot:[8]   Right:[]
     * Depth:2, Left:[5]   Pivot:[5]   Right:[6, 6]
     * Depth:3, Left:[6]   Pivot:[6]   Right:[]
   - Result of quick_sort()       : [0, 1, 2, 2, 3, 3, 5, 5, 6, 6, 8]
   - Result of sorted()           : [0, 1, 2, 2, 3, 3, 5, 5, 6, 6, 8]
   - Assert quick_sort == sorted(): True

"""

import copy

def quick_sort(l1):
    n = len(l1)
    if n < 2: return l1
    return quick_sort_partition(l1, 0, n-1)


def quick_sort_partition(l1, s, e, depth=0):
    if s < e:
        p = partition(l1, s, e)
        print_partition(l1, s, p, e, depth)
        quick_sort_partition(l1, s, p-1, depth+1)
        quick_sort_partition(l1, p+1, e, depth+1)
    return l1
    

def partition(l1, s, e):
    p, l, r = s, s+1, e
    while l <= r:
        while l <= r and l1[l] <= l1[p]: l += 1
        while l <= r and l1[p] <  l1[r]: r -= 1
        if l <= r: l1[l], l1[r] = l1[r], l1[l]
    l1[p], l1[r] = l1[r], l1[p]
    return r


def print_partition(l1, s, p, e, depth):
    seq1, pivot, seq2 = [], [l1[p]], []
    for v in range(s, p):
        seq1.append(l1[v])
    for v in range(p+1, e+1):
        seq2.append(l1[v])
    print(f"     * Depth:{depth}, Left:{seq1}   Pivot:{pivot}   Right:{seq2}")


def test():
    test_cases = [
        [],
        [2],
        [3, 2],
        [2, 3, 1],
        [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    ]
    for i, l1 in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : {l1}")
        res1 = quick_sort(copy.deepcopy(l1))
        res2 = sorted(l1)

        print(f"   - Result of quick_sort()       : {res1}")
        print(f"   - Result of sorted()           : {res2}")
        print(f"   - Assert quick_sort == sorted(): {res1 == res2}")


if __name__ == '__main__':
    test()

