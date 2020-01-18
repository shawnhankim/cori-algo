"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows

"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        negative = x < 0
        x = abs(x)
        
        while x > 0:
            res = res*10 + x % 10
            x //= 10
        if res > (2**31 -1):
            return 0
        return res if not negative else -res

sol = Solution()
test_cases = [123, -123, 1200]

for test_case in test_cases:
    print(f"{test_case} : {sol.reverse(test_case)}")

