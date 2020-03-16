"""
Insertion Sort

Expected Results:

1. test case : [11, 3, 28, 43, 9, 4]
   - Start insertion sort
     1) [3, 11, 28, 43, 9, 4]
     2) [3, 11, 28, 43, 9, 4]
     3) [3, 11, 28, 43, 9, 4]
     4) [3, 9, 11, 28, 43, 4]
     5) [3, 4, 9, 11, 28, 43]
   - Finish insertion sort
   - Iterative Insertion Sort Result : [3, 4, 9, 11, 28, 43]
   - Recursive Insertion Sort Result : [3, 4, 9, 11, 28, 43]
   - Iterative/Recursive insertion_sort() == sorted(l) : True

2. test case : [5, 3, 4, 1, 2]
   - Start insertion sort
     1) [3, 5, 4, 1, 2]
     2) [3, 4, 5, 1, 2]
     3) [1, 3, 4, 5, 2]
     4) [1, 2, 3, 4, 5]
   - Finish insertion sort
   - Iterative Insertion Sort Result : [1, 2, 3, 4, 5]
   - Recursive Insertion Sort Result : [1, 2, 3, 4, 5]
   - Iterative/Recursive insertion_sort() == sorted(l) : True

"""

import copy

def insertion_sort(l):
    print("   - Start insertion sort")
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j-1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]
            j -= 1
        print(f"     {i}) {l}")
    print("   - Finish insertion sort")
    return l


def insertion_sort_recursive(l, i=None):
    if i is None:
        i = len(l)-1
    if i <= 0:
        return l
    l = insertion_sort_recursive(l, i-1)
    j = i
    while j > 0 and l[j-1] > l[j]:
        l[j-1], l[j] = l[j], l[j-1]
        j -= 1
    return l
    

def test():
    test_case = [
        [11, 3, 28, 43, 9, 4],
        [5, 3, 4, 1, 2]
    ]
    for i, l in enumerate(test_case, 1):
        print(f"\n{i}. test case : {l}")
        res1 = insertion_sort(copy.deepcopy(l))
        print(f"   - Iterative Insertion Sort Result : {res1}")

        res2 = insertion_sort_recursive(copy.deepcopy(l))
        print(f"   - Recursive Insertion Sort Result : {res2}")

        res3 = sorted(copy.deepcopy(l))
        print(f"   - Iterative/Recursive insertion_sort() == sorted(l) : {res1 == res2 == res3}")


if __name__ == '__main__':
    test()

        
