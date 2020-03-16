
import numpy

def quick_select_search(l1, k):
    n = len(l1)
    if n < 1: return []
    if n < 2: return l1[0]
    
    p = n >> 1
    pivot = l1[p]
    l = [v for i, v in enumerate(l1) if v <= pivot and i != p]
    r = [v for i, v in enumerate(l1) if pivot <  v and i != p]

    m = len(l)
    if   k == m: return pivot 
    elif k <  m: return quick_select_search(l, k)
    else       : return quick_select_search(r, k-m-1)


def test():
    test_cases = [
        [],
        [2],
        [3, 2],
        [3, 1, 2],
        [3, 7, 2, 1, 4, 6, 5, 10, 9, 11]
    ]
    for i, l1 in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : {l1}")
        k = len(l1) >> 1
        res1 = quick_select_search(l1, k)
        res2 = sorted(l1)
        print(f"   - sorted()      : {res2}")
        print(f"   - qselect median: {res1}")

        median = numpy.median(l1) if len(l1) > 0 else []
        print(f"   - numpy median  : {median}")


if __name__ == '__main__':
    test()

