"""
Selection Sort: O(N^2)

Expected Results:

1. Test Case : [11, 3, 28, 43, 9, 4]
   ----- starting process of selection sort -----
   0) [11, 3, 28, 43, 9, 4]
   1) [3, 11, 28, 43, 9, 4]
   2) [3, 4, 28, 43, 9, 11]
   3) [3, 4, 9, 43, 28, 11]
   4) [3, 4, 9, 11, 28, 43]
   5) [3, 4, 9, 11, 28, 43]
   ----- complete process of selection sort -----

2. Test Case : [4, 9, 30, 22, 2, 1]
   ----- starting process of selection sort -----
   0) [4, 9, 30, 22, 2, 1]
   1) [1, 9, 30, 22, 2, 4]
   2) [1, 2, 30, 22, 9, 4]
   3) [1, 2, 4, 22, 9, 30]
   4) [1, 2, 4, 9, 22, 30]
   5) [1, 2, 4, 9, 22, 30]
   ----- complete process of selection sort -----

3. Test Case : []
   ----- starting process of selection sort -----
   ----- complete process of selection sort -----

4. Test Case : [5]
   ----- starting process of selection sort -----
   0) [5]
   ----- complete process of selection sort -----

5. Test Case : [2, 3]
   ----- starting process of selection sort -----
   0) [2, 3]
   1) [2, 3]
   ----- complete process of selection sort -----

6. Test Case : [9, 8]
   ----- starting process of selection sort -----
   0) [9, 8]
   1) [8, 9]
   ----- complete process of selection sort -----

"""

import math

def selection_sort(l):
    n = len(l)

    print("   ----- starting process of selection sort -----")
    for i in range(n):
        print(f"   {i}) {l}") 
        min_val, min_idx = l[i], i
        for j in range(i+1, n):
            if l[j] < min_val:
                min_idx = j
                min_val = l[j]
        l[i], l[min_idx] = l[min_idx], l[i]
    print("   ----- complete process of selection sort -----")


def test():
    test_cases = [
        [11, 3, 28, 43, 9, 4],
        [ 4, 9, 30, 22, 2, 1],
        [],
        [5],
        [2, 3],
        [9, 8]
    ]
    for i, l in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : {l}")
        selection_sort(l)


if __name__ == '__main__':
    test()

