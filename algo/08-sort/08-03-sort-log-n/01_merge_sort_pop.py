"""

Merge Sort w/ List Pop : O(n log n)

Expected Results :

1. Test Case : [4, 3, 1, 5, 2]
     * [3, 4]
     * [2, 5]
     * [1, 2, 5]
     * [1, 2, 3, 4, 5]
   - Merge Sort Result : [1, 2, 3, 4, 5]
   - merge_sort_pop() == sorted() : True

2. Test Case : [7, 5, 6, 2]
     * [5, 7]
     * [2, 6]
     * [2, 5, 6, 7]
   - Merge Sort Result : [2, 5, 6, 7]
   - merge_sort_pop() == sorted() : True

3. Test Case : []
   - Merge Sort Result : []
   - merge_sort_pop() == sorted() : True

4. Test Case : [2]
   - Merge Sort Result : [2]
   - merge_sort_pop() == sorted() : True

5. Test Case : [3, 2]
     * [2, 3]
   - Merge Sort Result : [2, 3]
   - merge_sort_pop() == sorted() : True

6. Test Case : [5, 2, 3]
     * [2, 3]
     * [2, 3, 5]
   - Merge Sort Result : [2, 3, 5]
   - merge_sort_pop() == sorted() : True

"""

import copy

def merge_sort_pop(seq):
    if len(seq) < 2: return seq
    m = len(seq) >> 1
    l, r = seq[:m], seq[m:]
    if len(l) > 1: l = merge_sort_pop(l)
    if len(r) > 1: r = merge_sort_pop(r)

    res = []
    while l and r:
        if l[-1] >= r[-1]: res.append(l.pop())
        else             : res.append(r.pop())
    res.reverse()
    res = (l or r) + res
    print(f"     * {res}")
    return res

def test():
    test_cases = [
        [4, 3, 1, 5, 2],
        [7, 5, 6, 2],
        [],
        [2],
        [3, 2],
        [5, 2, 3]
    ]
    for i, seq in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : {seq}")
        res1 = merge_sort_pop(copy.deepcopy(seq))
        print(f"   - Merge Sort Result : {res1}")
   
        res2 = sorted(copy.deepcopy(seq))
        print(f"   - merge_sort_pop() == sorted() : {res1 == res2}")


if __name__ == '__main__':
    test()

