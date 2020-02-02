"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

class Solution(object):
    def is_valid(self, s):
        hs = {')':'(', '}':'{', ']':'['}
        st = []
        for c in s:
            if c in hs:
                if not st or st.pop() != hs[c]:
                    return False
            else:
                st.append(c)
        return True if len(st) == 0 else False
                    
    def test(self):
        test_cases = ["()", "()[]{}", "{[", "([)]", "{[]}"]
        for i, test_case in enumerate(test_cases, 1):
            res = self.is_valid(test_case)
            print(f"{i}. Is valid ? {res} for test case: {test_case}")

if __name__ == '__main__':
    Solution().test()

  
