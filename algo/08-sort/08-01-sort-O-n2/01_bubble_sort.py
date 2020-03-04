"""
Bubble Sort

Time Complexity: O(N^2)

Expected Results:

1. Test Case : [11, 3, 28, 43, 9, 4]
   - sorted(l) == bubble_sort(l) -> True
   - bubble sort result -> [3, 4, 9, 11, 28, 43]

2. Test Case : [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
   - sorted(l) == bubble_sort(l) -> True
   - bubble sort result -> [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]

3. Test Case : []
   - sorted(l) == bubble_sort(l) -> True
   - bubble sort result -> []

4. Test Case : [2]
   - sorted(l) == bubble_sort(l) -> True
   - bubble sort result -> [2]

5. Test Case : [5, 3]
   - sorted(l) == bubble_sort(l) -> True
   - bubble sort result -> [3, 5]

6. Test Case : [5, 10, 2]
   - sorted(l) == bubble_sort(l) -> True
   - bubble sort result -> [2, 5, 10]

"""

def bubble_sort(l):
    n = len(l)
    if n <= 1: return l

    for k in range(n-1, -1, -1):
        for i in range(k):
            if l[i] > l[i+1]: 
                l[i], l[i+1] = l[i+1], l[i]
    return l


def test():
    test_cases = [
        [11, 3, 28, 43, 9, 4],
        [4, 5, 2, 1, 6, 2, 7, 10, 13, 8],
        [],
        [2],
        [5, 3],
        [5, 10, 2]
    ]
    for i, l in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : {l}")
        res1 = sorted(l)
        res2 = bubble_sort(l)
        print(f"   - sorted(l) == bubble_sort(l) -> {res1 == res2}")
        print(f"   - bubble sort result -> {res2}")

if __name__ == '__main__':
    test()

