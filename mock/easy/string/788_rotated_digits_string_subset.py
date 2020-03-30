"""
788. Rotated Digits

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].

Expected Results:

1. Test Case: {'N': 10, 'expected': 4}
   - Result 1 : 4
   - Result 2 : 4
   - Assert   : True

2. Test Case: {'N': 10000, 'expected': 2320}
   - Result 1 : 2320
   - Result 2 : 2320
   - Assert   : True
"""

class Solution:
    def rotatedDigits1(self, N):
        res = 0
        for i in range(N+1):
            s = str(i)
            if any([True if c in '347' else False for c in s]): continue
            if all([True if c in '018' else False for c in s]): continue
            res += 1
        return res

    def rotatedDigits2(self, N):
        res = 0
        for i in range(N+1):
            c = str(i)
            if not set('347').intersection(set(c)) and not set(c).issubset(set('018')):
                res += 1
        return res

    def test(self):
        test_cases = [
            {"N":    10, "expected": 4},
            {"N": 10000, "expected": 2320}
        ]
        for i, test_case in enumerate(test_cases, 1):
            N, expected = test_case['N'], test_case['expected']
            print(f"\n{i}. Test Case: {test_case}")
            res1 = self.rotatedDigits1(N)
            res2 = self.rotatedDigits2(N)
            print(f"   - Result 1 : {res1}")
            print(f"   - Result 2 : {res2}")
            print(f"   - Assert   : {expected == res1 == res2}")


if __name__ == '__main__':
    Solution().test()

 


