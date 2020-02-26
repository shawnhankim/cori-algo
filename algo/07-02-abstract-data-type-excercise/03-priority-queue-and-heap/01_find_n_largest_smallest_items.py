"""
Find n smallest or largest items using heap
"""

import heapq as hq


def find_n_largest_items(n, items):
    return hq.nlargest(n, items)


def find_n_smallest_items(n, items):
    return hq.nsmallest(n, items)


def find_smallest_items_seq_heap(items):
    hq.heapify(items)
    return hq.heappop(items)


def find_smallest_item(items):
    return min(items)


def find_n_smallest_items_seq_sorted(n, items):
    return sorted(items)[:n]


def find_n_largest_items_seq_sorted(n, items):
    return sorted(items)[len(items)-n:]


def test():
    items = [1, 3, 2, 8, 6, 10, 9]
    n = 3
    assert(find_n_largest_items            (n, items) == [10, 9,  8])
    assert(find_n_largest_items_seq_sorted (n, items) == [ 8, 9, 10])
    assert(find_n_smallest_items           (n, items) == [ 1, 2,  3])
    assert(find_n_smallest_items_seq_sorted(n, items) == [ 1, 2,  3])
    assert(find_smallest_item              (items)    == 1)
    assert(find_smallest_items_seq_heap    (items)    == 1)
    print("Test has been passed.")


if __name__ == '__main__':
    test()


