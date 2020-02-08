"""
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict = {}
        for i, num in enumerate(nums):
           val = target - num
           if val in dict:
               return [dict[val], i]
           dict[num] = i
        return []

sol = Solution()
test_cases = [
    [ [2, 7, 11, 15],  9 ],
    [ [1, 5,  9, 20], 25 ]
]

for test_case in test_cases:
    res = sol.two_sum(test_case[0], test_case[1])
    print(res)

