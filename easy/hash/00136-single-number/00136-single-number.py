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

"""

class Solution(object):
    def single_number1(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res

    def single_number2(self, nums):
        hs = set()
        for num in nums:
            if num in hs:
                hs.remove(num)
            else:
                hs.add(num)
        return list(hs)[0]

    def single_number3(self, nums):
        hs = {}
        for num in nums:
            if num in hs:
                del hs[num]
            else:
                hs[num] = True
        return next(iter(hs))

    def test(self):
        test_cases = [
            [2,2,1],
            [4,1,2,1,2],
            [2]
        ]
        for i, test_case in enumerate(test_cases, 1):
            res = self.single_number1(nums=test_case)
            print(f"{i}. single number1 : {res} for {test_case}")

            res = self.single_number2(nums=test_case)
            print(f"   single_number2 : {res} for {test_case}")

            res = self.single_number3(nums=test_case)
            print(f"   single_number3 : {res} for {test_case}\n")

if __name__ == "__main__":
    Solution().test()
