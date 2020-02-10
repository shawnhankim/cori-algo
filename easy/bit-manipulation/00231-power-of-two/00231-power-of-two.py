"""
231. Power of Two

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false

Expected Result:
0. is  -1 power of two ? False
1. is   0 power of two ? False
2. is   1 power of two ? True
3. is   2 power of two ? True
4. is   3 power of two ? False
5. is  16 power of two ? True
6. is 231 power of two ? False
"""

import math

class Solution(object):
    def is_power_of_two(self, n):
        if n <= 0: return False
        cnt, t = int(math.log(n, 2)) + 1, 0
        for _ in range(cnt):
            if n & 1: t += 1
            if t > 1: return False
            n >>= 1
        return t == 1


    def test(self):
        test_cases = [-1, 0, 1, 2, 3, 16, 231]
        for i, n in enumerate(test_cases):
            res = self.is_power_of_two(n)
            print(f"{i}. is {n:3} power of two ? {res}")


if __name__ == '__main__':
    Solution().test()

