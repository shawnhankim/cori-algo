"""
349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

Expected Result:

0. intersection of [1, 2, 2, 1] and [2, 2] -> [2], [2]
1. intersection of [4, 9, 5] and [9, 4, 9, 8, 4] -> [9, 4], [4, 9]

"""

class Solution(object):
    def intersection1(self, nums1, nums2):
        res, hs = [], {}
        for n in nums1:
            if n not in hs: hs[n] = 1
        for n in nums2:
            if n in hs: 
                res.append(n)
                del hs[n]
        return res


    def intersection2(self, nums1, nums2):
        res, hs, i, j = [], {}, 0, 0
        nums1, nums2 = sorted(nums1), sorted(nums2)
        while i < len(nums1) and j < len(nums2):
            a, b = nums1[i], nums2[j]
            if a == b:
                if a not in hs:
                    hs[a] = 1
                    res.append(a)
                i, j = i+1, j+1
            elif a > b: j += 1
            elif a < b: i += 1
        return res


    def test(self):
        test_cases = [
            {"nums1": [1,2,2,1], "nums2": [2,2]},
            {"nums1": [4,9,5]  , "nums2": [9,4,9,8,4]}
        ]
        for i, test_case in enumerate(test_cases):
            nums1 = test_case['nums1']
            nums2 = test_case['nums2']
            res1  = self.intersection1(nums1, nums2)
            res2  = self.intersection2(nums1, nums2)
            print(f"{i}. intersection of {nums1} and {nums2} -> {res1}, {res2}")


if __name__ == '__main__':
    Solution().test()
 
