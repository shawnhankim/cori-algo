"""
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

Expected Result:
0. anagram    vs. nagaram    -> Is anagram ? result-1:True, result-2:True
1. rat        vs. car        -> Is anagram ? result-1:False, result-2:False

"""

class Solution(object):
    def is_anagram1(self, s, t):
        return False if len(s) != len(t) else sorted(s) == sorted(t)


    def is_anagram2(self, s, t):
        hs = {}
        for c in s:
            if c in hs: hs[c] += 1
            else      : hs[c]  = 1
        for c in t:
            if c in hs:
                if hs[c] > 1: hs[c] -= 1
                else        : del hs[c]
            else:
                return False
        return True if not len(hs) else False


    def test(self):
        test_cases = [
            {"s": "anagram", "t": "nagaram"},
            {"s": "rat"    , "t": "car"    }
        ]
        for i, test_case in enumerate(test_cases):
            s, t = test_case['s'], test_case['t']
            res1 = self.is_anagram1(s, t)
            res2 = self.is_anagram2(s, t)
            print(f"{i}. {s:10} vs. {t:10} -> Is anagram ? result-1:{res1}, result-2:{res2}")


if __name__ == '__main__':
    Solution().test()

         
