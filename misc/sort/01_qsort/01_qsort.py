"""
Quick Sort

[4, 1, 2, 3]

[] [4] [1,2,3]

"""

class Solution(object):
    
    def qsort(self, array):
        if len(array) < 2:
            return array
        pivot = array[0]
        lesser  = [ele for ele in array[1:] if ele <= pivot]
        greater = [ele for ele in array[1:] if ele >  pivot]
        return self.qsort(lesser) + [pivot] + self.qsort(greater)

    def test(self):
        test_cases = [
            [4, 1, 2],
            [4, 1, 2, 3],
            [5, 7, 2, 3, 6],
            [1],
            [],
            ['Z', 'A', 'B'],
            ['spyder', 'ironman', 'antman']
        ]
        for i, test_case in enumerate(test_cases, 1):
            print(f"\ntest-{i}. {test_case}")
            print(f"  - qsort : {self.qsort(test_case)}")
        print()

Solution().test()
