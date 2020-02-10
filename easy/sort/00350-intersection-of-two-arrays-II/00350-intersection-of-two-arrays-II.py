"""
350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

Expected Result:
1. Intersection of [1, 2, 2, 1] and [2, 2] -> [2, 2]
2. Intersection of [4, 9, 5] and [9, 4, 9, 8, 4] -> [4, 9]
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        if not nums1 or not nums2: return []
        res = []
        if len(nums1) > len(nums2): return self.helper(nums2, nums1, res)
        return self.helper(nums1, nums2, res)


    def helper(self, nums1, nums2, res):
        hs = {}
        for n in nums1:
            if n not in hs: hs[n]  = 1
            else          : hs[n] += 1
        for n in nums2:
            if n in hs and hs[n] > 0:
                res.append(n)
                hs[n] -= 1
        return sorted(res)


    def test(self):
        test_cases = [
            {"nums1": [1,2,2,1], "nums2": [2,2]},
            {"nums1": [4,9,5]  , "nums2": [9,4,9,8,4]} 
        ]                
        for i, test_case in enumerate(test_cases, 1):
            nums1, nums2 = test_case['nums1'], test_case['nums2']
            res = self.intersect(nums1, nums2)
            print(f"{i}. Intersection of {nums1} and {nums2} -> {res}")


if __name__ == '__main__':
    Solution().test()

            
