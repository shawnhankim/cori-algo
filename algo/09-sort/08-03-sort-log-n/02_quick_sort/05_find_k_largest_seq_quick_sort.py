"""

Find K'th largest list using quick sort like algorithm

Expected Results:

1. Test Case : k:3, list:[]
    - Current sort until finding k : []
    - Result of k largest sequence : []

2. Test Case : k:3, list:[2]
    - Current sort until finding k : [2]
    - Result of k largest sequence : []

3. Test Case : k:3, list:[3, 2]
    - Current sort until finding k : [3, 2]
    - Result of k largest sequence : []

4. Test Case : k:3, list:[2, 3, 1]
       * Depth 0: Left: [1],   Pivot: 2, Right: [3]
    - Current sort until finding k : [1, 2, 3]
    - Result of k largest sequence : [1, 2, 3]

5. Test Case : k:3, list:[3, 10, 4, 5, 1, 8, 9, 11, 5]
       * Depth 0: Left: [1],   Pivot: 3, Right: [4, 5, 10, 8, 9, 11, 5]
       * Depth 1: Left: [1, 3],   Pivot: 4, Right: [5, 10, 8, 9, 11, 5]
       * Depth 2: Left: [1, 3, 4, 5],   Pivot: 5, Right: [8, 9, 11, 10]
       * Depth 3: Left: [1, 3, 4, 5, 5],   Pivot: 8, Right: [9, 11, 10]
       * Depth 4: Left: [1, 3, 4, 5, 5, 8],   Pivot: 9, Right: [11, 10]
    - Current sort until finding k : [1, 3, 4, 5, 5, 8, 9, 11, 10]
    - Result of k largest sequence : [9, 11, 10]

6. Test Case : k:3, list:[1, 2, 3, 3, 4, 4, 4, 5]
       * Depth 0: Left: [],   Pivot: 1, Right: [2, 3, 3, 4, 4, 4, 5]
       * Depth 1: Left: [1],   Pivot: 2, Right: [3, 3, 4, 4, 4, 5]
       * Depth 2: Left: [1, 2, 3],   Pivot: 3, Right: [4, 4, 4, 5]
       * Depth 3: Left: [1, 2, 3, 3, 4, 4],   Pivot: 4, Right: [5]
       * Depth 4: Left: [1, 2, 3, 3, 4],   Pivot: 4, Right: [4, 5]
    - Current sort until finding k : [1, 2, 3, 3, 4, 4, 4, 5]
    - Result of k largest sequence : [4, 4, 5]

"""

import random

def find_k_largest_seq_quick_sort(l1, k):
    n = len(l1)
    m = n - k
    if n < m or len(l1) < 1 or m < 0: return []
    quick_select(l1, k, 0, n-1)

    res = []
    for i in range(m, n):
        res.append(l1[i])
    return res


def partition(l1, s, e, depth=0):
    p, l, r = s, s+1, e
    while l <= r:
        while l <= r and l1[l] <= l1[p]: l += 1
        while l <= r and l1[p] <  l1[r]: r -= 1
        if l <= r: l1[l], l1[r] = l1[r], l1[l]
    l1[p], l1[r] = l1[r], l1[p]
    return r
    

def quick_select(l1, k, s, e, depth=0):
    if s < e:
        p = partition(l1, s, e, depth+1)
        print_list(l1, p, depth)
        if p == len(l1)-k: return l1

        quick_select(l1, k, s, p-1, depth+1)
        quick_select(l1, k, p+1, e, depth+1)
    return l1


def print_list(l1, p, depth):
    res = []
    for i in range(p):
        res.append(l1[i])
    print(f"       * Depth {depth}: Left: {res},   Pivot: {l1[p]}, ", end="")

    res = []
    for i in range(p+1, len(l1)):
        res.append(l1[i])
    print(f"Right: {res}")


def test_find_k_largest_seq_quick_sort():
    test_cases = [
        [],
        [2],
        [3, 2],
        [2, 3, 1],
        [3, 10, 4, 5, 1, 8, 9, 11, 5],
        [1, 2, 3, 3, 4, 4, 4, 5]
    ]
    k = 3
    for i, l1 in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : k:{k}, list:{l1}")
        res = find_k_largest_seq_quick_sort(l1, k)
        print(f"    - Current sort until finding k : {l1}") 
        print(f"    - Result of k largest sequence : {res}")


if __name__ == '__main__':
    test_find_k_largest_seq_quick_sort()

