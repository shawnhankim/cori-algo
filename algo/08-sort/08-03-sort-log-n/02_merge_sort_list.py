"""

Merge Sort by List : O(N log N)

Expected Results: 

1. Test Case : []
   - Result of merge_sort_list() : []
   - Result of sorted()          : []
   - Assert merge_sort_list() == sorted() : True

2. Test Case : [2]
   - Result of merge_sort_list() : [2]
   - Result of sorted()          : [2]
   - Assert merge_sort_list() == sorted() : True

3. Test Case : [2, 1]
     * depth: 0. [2] + [1] -> [1, 2]
   - Result of merge_sort_list() : [1, 2]
   - Result of sorted()          : [1, 2]
   - Assert merge_sort_list() == sorted() : True

4. Test Case : [2, 2, 3, 1]
     * depth: 1. [2] + [2] -> [2, 2]
     * depth: 1. [3] + [1] -> [1, 3]
     * depth: 0. [2, 2] + [1, 3] -> [1, 2, 2, 3]
   - Result of merge_sort_list() : [1, 2, 2, 3]
   - Result of sorted()          : [1, 2, 2, 3]
   - Assert merge_sort_list() == sorted() : True

5. Test Case : [3, 5, 2, 6, 7, 1, 0, 3, 5, 6, 2]
     * depth: 2. [3] + [5] -> [3, 5]
     * depth: 3. [6] + [7] -> [6, 7]
     * depth: 2. [2] + [6, 7] -> [2, 6, 7]
     * depth: 1. [3, 5] + [2, 6, 7] -> [2, 3, 5, 6, 7]
     * depth: 3. [0] + [3] -> [0, 3]
     * depth: 2. [1] + [0, 3] -> [0, 1, 3]
     * depth: 3. [6] + [2] -> [2, 6]
     * depth: 2. [5] + [2, 6] -> [2, 5, 6]
     * depth: 1. [0, 1, 3] + [2, 5, 6] -> [0, 1, 2, 3, 5, 6]
     * depth: 0. [2, 3, 5, 6, 7] + [0, 1, 2, 3, 5, 6] -> [0, 1, 2, 2, 3, 3, 5, 5, 6, 6, 7]
   - Result of merge_sort_list() : [0, 1, 2, 2, 3, 3, 5, 5, 6, 6, 7]
   - Result of sorted()          : [0, 1, 2, 2, 3, 3, 5, 5, 6, 6, 7]
   - Assert merge_sort_list() == sorted() : True

6. Test Case : [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]
     * depth: 3. [1] + [2] -> [1, 2]
     * depth: 2. [1] + [1, 2] -> [1, 1, 2]
     * depth: 3. [3] + [3] -> [3, 3]
     * depth: 2. [3] + [3, 3] -> [3, 3, 3]
     * depth: 1. [1, 1, 2] + [3, 3, 3] -> [1, 1, 2, 3, 3, 3]
     * depth: 3. [5] + [5] -> [5, 5]
     * depth: 2. [4] + [5, 5] -> [4, 5, 5]
     * depth: 3. [5] + [6] -> [5, 6]
     * depth: 3. [7] + [8] -> [7, 8]
     * depth: 2. [5, 6] + [7, 8] -> [5, 6, 7, 8]
     * depth: 1. [4, 5, 5] + [5, 6, 7, 8] -> [4, 5, 5, 5, 6, 7, 8]
     * depth: 0. [1, 1, 2, 3, 3, 3] + [4, 5, 5, 5, 6, 7, 8] -> [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]
   - Result of merge_sort_list() : [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]
   - Result of sorted()          : [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]
   - Assert merge_sort_list() == sorted() : True

"""

def merge_sort_list(l1, depth=0):
    n = len(l1)
    if n < 2: return l1
    
    m = n >> 1
    l = merge_sort_list(l1[:m], depth+1)
    r = merge_sort_list(l1[m:], depth+1)

    res = merge_lists(l, r)
    print(f"     * depth: {depth}. {l} + {r} -> {res}")
    return res


def merge_lists(l, r):
    if not l or not r: return r or l

    res, i, j, l_len, r_len = [], 0, 0, len(l), len(r)
    while l and r and i < l_len and j < r_len:
        if l[i] > r[j]:
            res.append(r[j])
            j += 1
        else:
            res.append(l[i])
            i += 1

    if not l[i:] or not r[j:]:
        res.extend(l[i:] or r[j:])

    return res


def test():
    test_cases = [
        [],
        [2],
        [2, 1],
        [2, 2, 3, 1],
        [3, 5, 2, 6, 7, 1, 0, 3, 5, 6, 2],
        [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]
    ]
    for i, l1 in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : {l1}")
        res1 = merge_sort_list(l1)
        res2 = sorted(l1)
        print(f"   - Result of merge_sort_list() : {res1}")
        print(f"   - Result of sorted()          : {res2}")
        print(f"   - Assert merge_sort_list() == sorted() : {res1 == res2}")


if __name__ == '__main__':
    test()

