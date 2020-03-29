"""
448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

Expected Results:

1. Test Case: [4, 3, 2, 7, 8, 2, 3, 1]
   - Result 1 : [5, 6]
   - Result 2 : [5, 6]
   - Result 3 : [5, 6]
   - Expected : [5, 6]
   - Assert   : True

2. Test Case: [2, 2]
   - Result 1 : [1]
   - Result 2 : [1]
   - Result 3 : [1]
   - Expected : [1]
   - Assert   : True

3. Test Case: [1, 1, 2, 2]
   - Result 1 : [3, 4]
   - Result 2 : [3, 4]
   - Result 3 : [3, 4]
   - Expected : [3, 4]
   - Assert   : True

4. Test Case: [39, 31, 8, 14, 14, 38, 5, 15, 29, 49, 18, 6, 30, 47, 8, 35, 2, 17, 6, 10, 29, 46, 41, 48, 1, 36, 5, 28, 46, 39, 7, 47, 18, 42, 17, 11, 36, 45, 21, 33, 24, 10, 24, 50, 25, 16, 9, 12, 11, 25]
   - Result 1 : [3, 4, 13, 19, 20, 22, 23, 26, 27, 32, 34, 37, 40, 43, 44]
   - Result 2 : [3, 4, 13, 19, 20, 22, 23, 26, 27, 32, 34, 37, 40, 43, 44]
   - Result 3 : [3, 4, 13, 19, 20, 22, 23, 26, 27, 32, 34, 37, 40, 43, 44]
   - Expected : [3, 4, 13, 19, 20, 22, 23, 26, 27, 32, 34, 37, 40, 43, 44]
   - Assert   : True

"""

from copy import deepcopy

class Solution:

    def findDisappearedNumbers1(self, nums):
        res, hs = [], set(nums)
        for i in range(1, len(nums)+1):
            if i not in hs: res.append(i)
        return res

    def findDisappearedNumbers2(self, nums):
        a = set(range(1, len(nums)+1))
        b = set(nums)
        return sorted(list(a-b))


    def findDisappearedNumbers3(self, nums):
        res = []
        nums.insert(0, 0)
        for i, c in enumerate(nums):  # i:idx, c: curr, n: next
            c = nums[i]

            # check if current index's number already exists
            if i == 0 or c < 0: continue
            
            # backup next index's number in array
            n = nums[c]

            # set -(current number) to next index in array
            nums[c] = -c
            
            # set 0 to current index in array
            nums[i] = 0

            # handle next number
            if n < 0: continue
            if i < n: res.append(n)
            else    : nums[n] = -n

        while res:
            n = res.pop()
            nums[n] = n
        
        for i, num in enumerate(nums):
            if i == 0: continue
            if num == 0: res.append(i)
        
        return res


    def test(self):
        test_cases = [
            { "nums"    : [4,3,2,7,8,2,3,1],
              "expected": [5,6]
            },
            { "nums"    : [2,2],
              "expected": [1]
            },
            { "nums"    : [1,1,2,2],
              "expected": [3,4]
            },
            { "nums"    : [39,31,8,14,14,38,5,15,29,49,18,6,30,47,8,35,2,17,6,10,29,46,41,48,1,36,5,28,46,39,7,47,18,42,17,11,36,45,21,33,24,10,24,50,25,16,9,12,11,25],
              "expected": [3,4,13,19,20,22,23,26,27,32,34,37,40,43,44]
            }
        ]
        
        for i, test_case in enumerate(test_cases, 1):
            nums, expected = test_case['nums'], test_case['expected']
            print(f"\n{i}. Test Case: {nums}")
            res1 = self.findDisappearedNumbers1(deepcopy(nums))
            res2 = self.findDisappearedNumbers2(deepcopy(nums))
            res3 = self.findDisappearedNumbers3(deepcopy(nums))
            print(f"   - Result 1 : {res1}")
            print(f"   - Result 2 : {res2}")
            print(f"   - Result 3 : {res3}")
            print(f"   - Expected : {expected}")
            print(f"   - Assert   : {res1 == res2 == res3 == expected}")


if __name__ == '__main__':
    Solution().test()

