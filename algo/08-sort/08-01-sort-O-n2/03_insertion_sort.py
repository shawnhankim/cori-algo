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
   - Result : [3, 4, 9, 11, 28, 43]
   - insertion_sort() == sorted(l) : True

2. test case : [5, 3, 4, 1, 2]
   - Start insertion sort
     1) [3, 5, 4, 1, 2]
     2) [3, 4, 5, 1, 2]
     3) [1, 3, 4, 5, 2]
     4) [1, 2, 3, 4, 5]
   - Finish insertion sort
   - Result : [1, 2, 3, 4, 5]
   - insertion_sort() == sorted(l) : True

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


def test():
    test_case = [
        [11, 3, 28, 43, 9, 4],
        [5, 3, 4, 1, 2]
    ]
    for i, l in enumerate(test_case, 1):
        print(f"\n{i}. test case : {l}")
        res1 = insertion_sort(copy.deepcopy(l))
        print(f"   - Result : {res1}")

        res2 = sorted(copy.deepcopy(l))
        print(f"   - insertion_sort() == sorted(l) : {res1 == res2}")


if __name__ == '__main__':
    test()

        
