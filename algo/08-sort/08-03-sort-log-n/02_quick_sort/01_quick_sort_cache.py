"""
Quick Sort : O(n Log n) ~ O(n^2)

Expected Results: 

1. Test Case : []
   - Result of quick_sort_cache()    : []
   - Result of sorted()              : []
   - Assert quick_sort() == sorted() : True

2. Test Case : [1]
   - Result of quick_sort_cache()    : [1]
   - Result of sorted()              : [1]
   - Assert quick_sort() == sorted() : True

3. Test Case : [2, 1]
     * depth 0. pivot: [2], left: [1], right: [] -> [1, 2]
   - Result of quick_sort_cache()    : [1, 2]
   - Result of sorted()              : [1, 2]
   - Assert quick_sort() == sorted() : True

4. Test Case : [2, 3, 1]
     * depth 0. pivot: [2], left: [1], right: [3] -> [1, 2, 3]
   - Result of quick_sort_cache()    : [1, 2, 3]
   - Result of sorted()              : [1, 2, 3]
   - Assert quick_sort() == sorted() : True

5. Test Case : [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
     * depth 2. pivot: [1], left: [0], right: [2] -> [0, 1, 2]
     * depth 1. pivot: [2], left: [1, 0, 2], right: [3] -> [0, 1, 2, 2, 3]
     * depth 2. pivot: [6], left: [6], right: [8] -> [6, 6, 8]
     * depth 1. pivot: [5], left: [5], right: [6, 8, 6] -> [5, 5, 6, 6, 8]
     * depth 0. pivot: [3], left: [2, 1, 0, 3, 2], right: [5, 6, 8, 5, 6] -> [0, 1, 2, 2, 3, 3, 5, 5, 6, 6, 8]
   - Result of quick_sort_cache()    : [0, 1, 2, 2, 3, 3, 5, 5, 6, 6, 8]
   - Result of sorted()              : [0, 1, 2, 2, 3, 3, 5, 5, 6, 6, 8]
   - Assert quick_sort() == sorted() : True

"""

import copy

def quick_sort_cache(l1, depth=0):
    if len(l1) < 2: return l1

    pivot_idx = 0
    pivot = l1[0]

    l = [x for i, x in enumerate(l1) if x <= pivot and i != pivot_idx]
    r = [x for i, x in enumerate(l1) if x >  pivot and i != pivot_idx]
    res = quick_sort_cache(l, depth+1) + [pivot] + quick_sort_cache(r, depth+1)
    print(f"     * depth {depth}. pivot: [{pivot}], left: {l}, right: {r} -> {res}")
    return res

def test():
    test_cases = [
        [],
        [1],
        [2, 1],
        [2, 3, 1],
        [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    ]
    for i, l1 in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : {l1}")
        res1 = quick_sort_cache(copy.deepcopy(l1))
        res2 = sorted(l1)

        print(f"   - Result of quick_sort_cache()    : {res1}")
        print(f"   - Result of sorted()              : {res2}")
        print(f"   - Assert quick_sort() == sorted() : {res1 == res2}")


if __name__ == '__main__':
    test()

