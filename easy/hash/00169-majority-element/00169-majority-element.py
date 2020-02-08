"""
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

"""

class Solution(object):
    def majority_element(self, nums):
        nset, maxn, res = {}, 0, 0
        for n in nums:
            if n in nset: nset[n] += 1
            else        : nset[n]  = 1
            if maxn < nset[n]:
                maxn = nset[n]
                res  = n
        return res


    def test(self):
        test_cases = [
            [3,2,3],
            [2,2,1,1,1,2,2]
        ]
        for i, test_case in enumerate(test_cases):
            res = self.majority_element(test_case)
            print(f"{i}. majority element: {res} <- {test_case}")


if __name__ == '__main__':
    Solution().test()

