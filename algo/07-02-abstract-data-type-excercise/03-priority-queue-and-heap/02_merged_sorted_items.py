"""
Merge Sorted Items using heapq

Expected Results:

1. merge [1, 2, 3, 8, 9, 10] & [2, 3, 4, 5, 6, 7, 9]
   - result 1 : [1, 2, 2, 3, 5, 7, 3, 8, 4, 9, 6, 10, 9]
   - result 2 : [1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 9, 10]

"""

import heapq as hq


def merge_sorted_items1(l1, l2):
    res = l1 + l2
    hq.heapify(res)
    return res


def merge_sorted_items2(l1, l2):
    res = []
    for c in hq.merge(l1, l2):
        res.append(c)
    return res


def test():
    test_cases = [
        {"l1": [1, 2, 3, 8, 9, 10], "l2": [2, 3, 4, 5, 6, 7, 9]}
    ]
    for i, test_case in enumerate(test_cases, 1):
        l1, l2 = test_case['l1'], test_case['l2']
        res1 = merge_sorted_items1(l1, l2)
        res2 = merge_sorted_items2(l1, l2)
        print(f"\n{i}. merge {str(l1):10} & {str(l2):10}")
        print(f"   - result 1 : {res1}")
        print(f"   - result 2 : {res2}")


if __name__ == '__main__':
    test()

