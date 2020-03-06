"""

Counting Sort : O(n + k)
   - n : number of elements
   - k : number of unique elements

Expected Results:

1. Test Case : [2, 2, 5, 3, 3, 4, 3]
   - Counting Sort 1 w/ O(N+K) : [2, 2, 3, 3, 3, 4, 5]
   - Counting Sort 2 w/ O(N+N) : [2, 2, 3, 3, 3, 4, 5]
   - Assert count_sort(l) == sorted(l) : True

2. Test Case : [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
   - Counting Sort 1 w/ O(N+K) : [0, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 6, 8]
   - Counting Sort 2 w/ O(N+N) : [0, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 6, 8]
   - Assert count_sort(l) == sorted(l) : True

"""

from collections import defaultdict
import copy

def counting_sort1(l):
    res, hs = [], defaultdict(list)

    for v in l:
        hs[v].append(v)
    for v in range(min(hs), max(hs)+1):
        res.extend(hs[v])
    return res


def counting_sort2(l):
    res, hs = [], {}

    for v in l:
        if v in hs: hs[v] += 1
        else      : hs[v]  = 1

    for v in range(min(hs), max(hs)+1):
        if v not in hs: continue
        for i in range(hs[v]):
            res.append(v)

    return res


def test():
    test_cases = [
        [2, 2, 5, 3, 3, 4, 3],
        [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
    ]
    for i, l in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : {l}")
        res1 = counting_sort1(copy.deepcopy(l))
        print(f"   - Counting Sort 1 w/ O(N+K) : {res1}")

        res2 = counting_sort2(copy.deepcopy(l))
        print(f"   - Counting Sort 2 w/ O(N+N) : {res2}")

        res3 = sorted(copy.deepcopy(l))
        print(f"   - Assert count_sort(l) == sorted(l) : {res1 == res2 == res3}")


if __name__ == '__main__':
    test()

