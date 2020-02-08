"""
136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

Expected Result:
0. Single Number :   1 <- [2, 2, 1]
1. Single Number :   4 <- [4, 1, 2, 1, 2]

"""

class Solution(object):
    def single_number(self, nums):
        res = 0
        for n in nums: res ^= n
        return res


    def test(self):
        test_cases = [
            [2,2,1],
            [4,1,2,1,2]
        ]
        for i, test_case in enumerate(test_cases):
            res = self.single_number(test_case)
            print(f"{i}. Single Number : {res:3} <- {test_case}")


if __name__ == '__main__':
    Solution().test()

