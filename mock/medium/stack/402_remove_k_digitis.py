"""
402. Remove K Digits
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:

The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Expected Results:

1. Test Case : {'k': 3, 'num': '1432219'}
   - Result : 1219

2. Test Case : {'k': 1, 'num': '10200'}
   - Result : 200

3. Test Case : {'k': 2, 'num': '10'}
   - Result : 0

4. Test Case : {'k': 1, 'num': '9'}
   - Result : 0

"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        for v in num:
            while k and stk and stk[-1] > v:
                stk.pop()
                k -= 1
            stk.append(v)
        return ''.join(stk[:len(stk)-k]).lstrip('0') or '0'

        
    def test(self):
        test_cases = [
            { "k": 3, "num": "1432219" },
            { "k": 1, "num": "10200"   },
            { "k": 2, "num": "10"      },
            { "k": 1, "num": "9"       }
        ]
        for i, test_case in enumerate(test_cases, 1):
            k, num = test_case['k'], test_case['num']
            print(f"\n{i}. Test Case : {test_case}")
            res = self.removeKdigits(num, k)
            print(f"   - Result : {res}")


if __name__ == '__main__':
    Solution().test()



