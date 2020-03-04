"""
Bubble Sort

Time Complexity: O(N^2)

Expected Results:

1. Test Case : [11, 3, 28, 43, 9, 4]
   ----- general bubble sort : O(N^2) -----
   - [11, 3, 28, 43, 9, 4]
   - [3, 11, 28, 9, 4, 43]
   - [3, 11, 9, 4, 28, 43]
   - [3, 9, 4, 11, 28, 43]
   - [3, 4, 9, 11, 28, 43]
   - [3, 4, 9, 11, 28, 43]
   - bubble sort result, O(6 * 6) -> [3, 4, 9, 11, 28, 43]

   ----- optimized bubble sort -----
   - [3, 4, 9, 11, 28, 43]
   - bubble sort result, O(1 * 1) -> [3, 4, 9, 11, 28, 43]

   ----- compare bubble sort vs. sorted() -----
   - sorted(l) == bubble_sort(l) -> True

2. Test Case : [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
   ----- general bubble sort : O(N^2) -----
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
   - bubble sort result, O(10 * 10) -> [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]

   ----- optimized bubble sort -----
   - [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]
   - bubble sort result, O(1 * 1) -> [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]

   ----- compare bubble sort vs. sorted() -----
   - sorted(l) == bubble_sort(l) -> True

3. Test Case : []
   ----- general bubble sort : O(N^2) -----
   - bubble sort result, O(0 * 0) -> []

   ----- optimized bubble sort -----
   - bubble sort result, O(0 * 0) -> []

   ----- compare bubble sort vs. sorted() -----
   - sorted(l) == bubble_sort(l) -> True

4. Test Case : [2]
   ----- general bubble sort : O(N^2) -----
   - bubble sort result, O(1 * 1) -> [2]

   ----- optimized bubble sort -----
   - bubble sort result, O(1 * 1) -> [2]

   ----- compare bubble sort vs. sorted() -----
   - sorted(l) == bubble_sort(l) -> True

5. Test Case : [5, 3]
   ----- general bubble sort : O(N^2) -----
   - [5, 3]
   - [3, 5]
   - bubble sort result, O(2 * 2) -> [3, 5]

   ----- optimized bubble sort -----
   - [3, 5]
   - bubble sort result, O(1 * 1) -> [3, 5]

   ----- compare bubble sort vs. sorted() -----
   - sorted(l) == bubble_sort(l) -> True

6. Test Case : [5, 10, 2]
   ----- general bubble sort : O(N^2) -----
   - [5, 10, 2]
   - [5, 2, 10]
   - [2, 5, 10]
   - bubble sort result, O(3 * 3) -> [2, 5, 10]

   ----- optimized bubble sort -----
   - [2, 5, 10]
   - bubble sort result, O(1 * 1) -> [2, 5, 10]

   ----- compare bubble sort vs. sorted() -----
   - sorted(l) == bubble_sort(l) -> True

7. Test Case : [1, 2, 4, 3]
   ----- general bubble sort : O(N^2) -----
   - [1, 2, 4, 3]
   - [1, 2, 3, 4]
   - [1, 2, 3, 4]
   - [1, 2, 3, 4]
   - bubble sort result, O(4 * 4) -> [1, 2, 3, 4]

   ----- optimized bubble sort -----
   - [1, 2, 3, 4]
   - bubble sort result, O(1 * 1) -> [1, 2, 3, 4]

   ----- compare bubble sort vs. sorted() -----
   - sorted(l) == bubble_sort(l) -> True

"""

def bubble_sort1(l):
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
        res3 = sorted(l)

        print(f"\n{i}. Test Case : {l}")
        print(f"   ----- general bubble sort : O(N^2) -----")
        res1, o_n = bubble_sort1(l)
        print(f"   - bubble sort result, O({o_n} * {o_n}) -> {res1}")

        print( "\n   ----- optimized bubble sort -----")
        res2, o_n = bubble_sort2(l)
        print(f"   - bubble sort result, O({o_n} * {o_n}) -> {res1}")

        print( "\n   ----- compare bubble sort vs. sorted() -----")
        print(f"   - sorted(l) == bubble_sort(l) -> {res1 == res2 == res3}")


if __name__ == '__main__':
    test()

