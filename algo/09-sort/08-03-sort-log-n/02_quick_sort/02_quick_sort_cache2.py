
import copy

def quick_sort_cache2(l1, depth=0):
    if len(l1) < 2: return l1
    l, p, r = get_left_pivot_right(l1)
    res = quick_sort_cache2(l, depth+1) + [p] + quick_sort_cache2(r, depth+1)
    print(f"     * depth {depth}. pivot: {p}, left: {l}, right: {r} -> {res}")
    return res

def get_left_pivot_right(l1):
    pivot = l1[0]
    l = [x for x in l1[1:] if x <= pivot]
    r = [x for x in l1[1:] if x >  pivot]
    return l, pivot, r


def test():
    test_cases = [
        [],
        [2],
        [3, 2],
        [5, 3, 4],
        [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    ]
    for i, l1 in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : {l1}")
        res1 = quick_sort_cache2(copy.deepcopy(l1))
        res2 = sorted(l1)

        print(f"   - Result of quick_sort_cache()  : {res1}")
        print(f"   - Result of sorted()            : {res2}")
        print(f"   - Assert quick_sort == sorted() : {res2 == res1}")


if __name__ == '__main__':
    test()


