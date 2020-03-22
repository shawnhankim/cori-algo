"""
46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

from copy import deepcopy
class Solution:
    def __init__(self):
        self.n = 0
        self.res = []
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.helper(nums, 0)
        return self.res
        
    def helper(self, nums, k):
        if k == self.n:
            self.res.append(deepcopy(nums))
        if k > self.n:
            return
        for i in range(k, self.n):
            self.swap(nums, i, k)
            self.helper(nums, k+1)
            self.swap(nums, i, k)
    
    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]

"""
    depth   0           1           2           nums        res
    ---------------------------------------------------------------
            i   k       i   k       i   k   
            0   0                               1 2 3
                        1   1                   1 2 3
                                    2   2       1 2 3       1 2 3
                        2   1                   1 3 2
                                    2   2       1 3 2       1 3 2
                                                1 2 3

            1   0                               2 1 3
                        1   1
                                    2   2       2 1 3       2 1 3
                        2   1                   2 3 1
                                    2   2       2 3 1       2 3 1
                        2   1                   2 1 3
            1   0                               1 2 3
            2   0                               3 2 1
                        1   1
                                    2   2       3 2 1       3 2 1
                        2   1                   3 1 2
                                    2   2       3 1 2       3 1 2

"""        

