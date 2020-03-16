"""
Gnome Sort

Expected Results:

1. Test Case : [3, 5, 2, 4]
   - Start gnome_sort()
     * i:1, [3, 5, 2, 4]
     * i:2, [3, 5, 2, 4]
     * i:1, [3, 2, 5, 4]
     * i:0, [2, 3, 5, 4]
     * i:1, [2, 3, 5, 4]
     * i:2, [2, 3, 5, 4]
     * i:3, [2, 3, 5, 4]
     * i:2, [2, 3, 4, 5]
     * i:3, [2, 3, 4, 5]
     * i:4, [2, 3, 4, 5]
   - Finish gnome_sort()
   - gnome sort result : [2, 3, 4, 5]
   - gnome_sort(l) == sorted(l) : True

2. Test Case : [1, 2, 3, 4]
   - Start gnome_sort()
     * i:1, [1, 2, 3, 4]
     * i:2, [1, 2, 3, 4]
     * i:3, [1, 2, 3, 4]
     * i:4, [1, 2, 3, 4]
   - Finish gnome_sort()
   - gnome sort result : [1, 2, 3, 4]
   - gnome_sort(l) == sorted(l) : True

"""

import copy

def gnome_sort(l):
    i = 0
    print("   - Start gnome_sort()")
    while i < len(l):
        if i == 0 or l[i-1] <= l[i]: i += 1
        else:
            l[i-1], l[i] = l[i], l[i-1]
            i -= 1
        print(f"     * i:{i}, {l}")
    print("   - Finish gnome_sort()") 
    return l


def test():
    test_cases = [
        [3, 5, 2, 4],
        [1, 2, 3, 4]
    ]
    for i, l in enumerate(test_cases, 1):
        print(f"\n{i}. Test Case : {l}")
        res1 = gnome_sort(copy.deepcopy(l))
        print(f"   - gnome sort result : {res1}")

        res2 = sorted(l)
        print(f"   - gnome_sort(l) == sorted(l) : {res1 == res2}")


if __name__ == '__main__':
    test()

