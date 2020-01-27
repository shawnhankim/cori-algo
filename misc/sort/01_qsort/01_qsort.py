"""
Quick Sort

[4, 1, 2, 3]

[] [4] [1,2,3]

"""

class Solution(object):
    
    def qsort(self, nums):
        if len(nums) < 2:
            return nums
        pivot = nums[0]
        lesser  = [num for num in nums[1:] if num <= pivot]
        greater = [num for num in nums[1:] if num >  pivot]
        return self.qsort(lesser) + [pivot] + self.qsort(greater)

    def test(self):
        test_cases = [
            [4, 1, 2],
            [4, 1, 2, 3],
            [5, 7, 2, 3, 6],
            [1],
            []
        ]
        for i, test_case in enumerate(test_cases, 1):
            print(f"\ntest-{i}. {test_case}")
            print(f"  - qsort : {self.qsort(test_case)}")
        print()

Solution().test()
