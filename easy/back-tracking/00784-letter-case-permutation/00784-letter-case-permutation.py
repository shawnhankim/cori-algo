"""
784. Letter Case Permutation

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.

Expected Result:
1. a1b2       -> ['a1b2', 'a1B2', 'A1b2', 'A1B2'], ['a1b2', 'A1b2', 'a1B2', 'A1B2']
2. 3z4        -> ['3z4', '3Z4'], ['3z4', '3Z4']
3. 12345      -> ['12345'], ['12345']
4.            -> [], ['']

"""

class Solution(object):
    def letter_case_permutation1(self, S):
        res = []
        if not S: return res
        return self.helper2(S, res, len(S))

 
    def helper(self, S, res, n, k=0, ele=""):
        if k == n: 
            res.append(ele)
            return res
        if k > n: return res
        
        c = S[k]
        ele += c
        res = self.helper(S, res, n, k+1, ele)
        ele = ele[:-1]

        alpha = self.change_alphabetic(c)
        if alpha:
            ele += alpha
            res = self.helper(S, res, n, k+1, ele)
            ele = ele[:-1]
        return res


    def helper2(self, S, res, n, k=0, ele=""):
        if k == n:
            res.append(ele)
            return res
        if S[k].isalpha():
            res = self.helper2(S, res, n, k+1, ele+S[k].lower())
            res = self.helper2(S, res, n, k+1, ele+S[k].upper())
        else:
            res = self.helper2(S, res, n, k+1, ele+S[k])
        return res


    def change_alphabetic(self, c):
        if 'a' <= c <= 'z': return c.upper()
        if 'A' <= c <= 'Z': return c.lower()
        return False


    def letter_case_permutation2(self, S):
        res = [""]
        if not S: return res

        for c in S:
            if c.isdigit():
                res = [ele + c for ele in res]
            else:
                t1 = [ele + c.lower() for ele in res]
                t2 = [ele + c.upper() for ele in res]
                res = t1 + t2
        return res


    def test(self):
        test_cases = ["a1b2", "3z4", "12345", ""]
        for i, test_case in enumerate(test_cases, 1):
            res1 = self.letter_case_permutation1(test_case)
            res2 = self.letter_case_permutation2(test_case)
            print(f"{i}. {test_case:10} -> {res1}, {res2}")


if __name__ == '__main__':
    Solution().test()

