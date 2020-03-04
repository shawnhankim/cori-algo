"""
Bubble Sort

Time Complexity: O(N^2)

Expected Results:

1. Test Case : [11, 3, 28, 43, 9, 4]
   - [11, 3, 28, 43, 9, 4]
   - [3, 11, 28, 9, 4, 43]
   - [3, 11, 9, 4, 28, 43]
   - [3, 9, 4, 11, 28, 43]
   - [3, 4, 9, 11, 28, 43]
   - [3, 4, 9, 11, 28, 43]
   - sorted(l) == bubble_sort(l) -> True
   - bubble sort result, O(6 * 6) -> [3, 4, 9, 11, 28, 43]
   - [3, 4, 9, 11, 28, 43]
   ----- optimized bubble sort -----
   - bubble sort result, O(1 * 1) -> [3, 4, 9, 11, 28, 43]

2. Test Case : [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
   - [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
   - [4, 2, 1, 5, 2, 6, 7, 10, 8, 13]
   - [2, 1, 4, 2, 5, 6, 7, 8, 10, 13]
   - [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]
   - [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]
   - [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]
   - [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]
   - [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]
   - [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]
   - [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]
   - sorted(l) == bubble_sort(l) -> True
   - bubble sort result, O(10 * 10) -> [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]
   - [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]
   ----- optimized bubble sort -----
   - bubble sort result, O(1 * 1) -> [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]

3. Test Case : []
   - sorted(l) == bubble_sort(l) -> True
   - bubble sort result, O(0 * 0) -> []
   ----- optimized bubble sort -----
   - bubble sort result, O(0 * 0) -> []

4. Test Case : [2]
   - sorted(l) == bubble_sort(l) -> True
   - bubble sort result, O(1 * 1) -> [2]
   ----- optimized bubble sort -----
   - bubble sort result, O(1 * 1) -> [2]

5. Test Case : [5, 3]
   - [5, 3]
   - [3, 5]
   - sorted(l) == bubble_sort(l) -> True
   - bubble sort result, O(2 * 2) -> [3, 5]
   - [3, 5]
   ----- optimized bubble sort -----
   - bubble sort result, O(1 * 1) -> [3, 5]

6. Test Case : [5, 10, 2]
   - [5, 10, 2]
   - [5, 2, 10]
   - [2, 5, 10]
   - sorted(l) == bubble_sort(l) -> True
   - bubble sort result, O(3 * 3) -> [2, 5, 10]
   - [2, 5, 10]
   ----- optimized bubble sort -----
   - bubble sort result, O(1 * 1) -> [2, 5, 10]

7. Test Case : [1, 2, 4, 3]
   - [1, 2, 4, 3]
   - [1, 2, 3, 4]
   - [1, 2, 3, 4]
   - [1, 2, 3, 4]
   - sorted(l) == bubble_sort(l) -> True
   - bubble sort result, O(4 * 4) -> [1, 2, 3, 4]
   - [1, 2, 3, 4]
   ----- optimized bubble sort -----
   - bubble sort result, O(1 * 1) -> [1, 2, 3, 4]

"""

def bubble_sort(l):
    n, o_n = len(l), 0
    if n <= 1: return l, n

    for k in range(n-1, -1, -1):
        o_n += 1
        print(f"   - {l}")
        for i in range(k):
            if l[i] > l[i+1]: 
                l[i], l[i+1] = l[i+1], l[i]
    return l, o_n


def bubble_sort2(l):
    n, o_n = len(l), 0
    if n < 2: return l, n

    for i in range(n-1, -1, -1):
        is_swap, o_n = False, o_n + 1
        print(f"   - {l}")
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                is_swap = True
        if not is_swap:
            break
    return l, o_n


def test():
    test_cases = [
        [11, 3, 28, 43, 9, 4],
        [4, 5, 2, 1, 6, 2, 7, 10, 13, 8],
        [],
        [2],
        [5, 3],
        [5, 10, 2],
        [1, 2, 4, 3]
    ]
    for i, l in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : {l}")
        res1 = sorted(l)
        res2, o_n = bubble_sort(l)
        print(f"   - sorted(l) == bubble_sort(l) -> {res1 == res2}")
        print(f"   - bubble sort result, O({o_n} * {o_n}) -> {res2}")

        res3, o_n = bubble_sort2(l)
        print( "   ----- optimized bubble sort -----")
        print(f"   - bubble sort result, O({o_n} * {o_n}) -> {res3}")


if __name__ == '__main__':
    test()

