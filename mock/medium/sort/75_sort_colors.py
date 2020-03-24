"""
75. Sort Colors
Medium

2606

194

Add to List

Share
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

class Solution:
    def sortColors(self, nums):
        l = m = 0
        r = len(nums) - 1
        
        while m <= r:
            if   nums[m] == 0:
                self.swap(nums, l, m)
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:
                self.swap(nums, r, m)
                r -= 1

        
    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]
        
    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
        
        k = 0
        for i, count in enumerate(counts):
            for j in range(k, k+count):
                nums[j] = i
            k += count
        
    
