"""

Recursive / Iterative Binary Search

Expected Results:

1. Test Case : target->6, list->[]
   - Result of recursive binary search: None
   - Result of iterative binary search: None

2. Test Case : target->6, list->[2, 6]
   - Result of recursive binary search: 1
   - Result of iterative binary search: 1

3. Test Case : target->6, list->[1, 2, 6, 8, 9, 10]
   - Result of recursive binary search: 2
   - Result of iterative binary search: 2

4. Test Case : target->6, list->[1, 2, 5, 6, 7, 10, 12, 12, 14, 15]
   - Result of recursive binary search: 3
   - Result of iterative binary search: 3
han:02-sorted-array-search devkim$ python 01_binary_search.py

1. Test Case : target->6, list->[]
   - Target index of recursive binary search: None
   - Target index of iterative binary search: None

2. Test Case : target->6, list->[2, 6]
   - Target index of recursive binary search: 1
   - Target index of iterative binary search: 1

3. Test Case : target->6, list->[1, 2, 6, 8, 9, 10]
   - Target index of recursive binary search: 2
   - Target index of iterative binary search: 2

4. Test Case : target->6, list->[1, 2, 5, 6, 7, 10, 12, 12, 14, 15]
   - Target index of recursive binary search: 3
   - Target index of iterative binary search: 3

"""

def binary_search_recursive(l1, target):
    if len(l1) < 1: return None
    return helper(l1, target, 0, len(l1)-1)


def helper(l1, target, l, r):
    if l > r: return None

    m = (l+r) >> 1
    if   target == l1[m]: return m
    elif target <  l1[m]: return helper(l1, target, l, m-1)
    else                : return helper(l1, target, m+1, r)


def binary_search_iterative(l1, target):
    if len(l1) < 1: return None

    l, r = 0, len(l1)-1
    while l <= r:
        m = (l+r) >> 1
        if   target == l1[m]: return m
        elif target <  l1[m]: r = m-1
        else                : l = m+1
    return None


def test():
    test_cases = [
        {"target": 6, "list": []},
        {"target": 6, "list": [2, 6]},
        {"target": 6, "list": [1, 2, 6, 8, 9, 10]},
        {"target": 6, "list": [1, 2, 5, 6, 7, 10, 12, 12, 14, 15]}
    ]
    for i, test_case in enumerate(test_cases, 1):
        target, l1 = test_case['target'], test_case['list']
        res1 = binary_search_recursive(l1, target)
        res2 = binary_search_iterative(l1, target)
        print(f"\n{i}. Test Case : target->{target}, list->{l1}")
        print(f"   - Target index of recursive binary search: {res1}")
        print(f"   - Target index of iterative binary search: {res2}")


if __name__ == '__main__':
    test()

