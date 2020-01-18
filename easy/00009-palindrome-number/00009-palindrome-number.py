"""
9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?

"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Time: O(n), Space: O(1) without converting integer to string
        
        # get length : O(n)
        # - l
        # - r
        
        # loop l > r : O(n/2)
        # get l value
        # get r value
        # return false if l != r
        
        # return true
        if x < 0:
            return False
        
        len = 0
        quotient = x
        while quotient > 0:
            quotient //= 10
            len += 1
        l = 0
        r = len - 1
        
        while l < r:
            l_value = x // (10 ** (r-l))
            r_value = x - (x // 10) * 10
            x = (x % (10 ** (r-l))) // 10
            if l_value != r_value:
                return False
            l += 1
            r -= 1
        return True
            

sol = Solution()
test_cases = [121, -121, 10, 999, 9999, 99899]

for test_case in test_cases:
    print(f"{test_case} : {sol.isPalindrome(test_case)}")

