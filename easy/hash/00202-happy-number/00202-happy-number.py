"""
202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

class Solution(object):
    def is_happy_number(self, n):
        hs = {}
        while True:
            n = sum(int(val)**2 for val in str(n))
            if n == 1:
                return True
            elif n in hs:
                return False
            hs[n] = True

    def test(self):
        test_cases = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 19]
        for i, test_case in enumerate(test_cases, 1):
            res = self.is_happy_number(test_case)
            print(f"[{i}. Is {test_case} happy number? {res}")

def main():
    Solution().test()

if __name__ == '__main__':
    main()

