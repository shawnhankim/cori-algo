"""

Quick Sort Algorithm based Search Median

Expected Results:

1. Test Case : []
   - sorted        : []
   - search_median : None
   - numpy median  : None

2. Test Case : [2]
   - sorted        : [2]
   - search_median : 2
   - numpy median  : 2.0

3. Test Case : [3, 2]
   - sorted        : [2, 3]
   - search_median : 3
   - numpy median  : 2.5

4. Test Case : [4, 2, 1, 3]
   - sorted        : [1, 2, 3, 4]
   - search_median : 3
   - numpy median  : 2.5

5. Test Case : [3, 7, 2, 1, 4, 6, 5, 10, 9, 11]
   - sorted        : [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]
   - search_median : 6
   - numpy median  : 5.5

"""

import numpy

def search_median(l1, k):
    n = len(l1)
    if n < 1: return None
    if n < 2: return l1[0]
    seq = search_median_helper(l1, k, 0, n-1)
    return seq[k]


def partition(l1, s, e):
    p, l, r = s, s+1, e
    while l <= r:
        while l <= r and l1[l] <= l1[p]: l += 1
        while l <= r and l1[p] <  l1[r]: r -= 1
        if l <= r: l1[l], l1[r] = l1[r], l1[l]
    l1[p], l1[r] = l1[r], l1[p]
    return r


def search_median_helper(l1, k, s, e):
    if s < e:
        p = partition(l1, s, e)
        if k == p: return l1
        search_median_helper(l1, k, s, p-1)
        search_median_helper(l1, k, p+1, e)
    return l1


def test():
    test_cases = [
        [],
        [2],
        [3, 2],
        [4, 2, 1, 3],
        [3, 7, 2, 1, 4, 6, 5, 10, 9, 11]
    ]
    for i, l1 in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : {l1}")
        k = len(l1) >> 1
        res1 = search_median(l1, k)
        res2 = sorted(l1)
        print(f"   - sorted        : {res2}")
        print(f"   - search_median : {res1}")

        median = numpy.median(l1) if len(l1) > 0 else None      
        print(f"   - numpy median  : {median}")


if __name__ == '__main__':
    test()


