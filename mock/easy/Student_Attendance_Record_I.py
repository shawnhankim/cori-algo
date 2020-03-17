"""
Student Attendance Record I

You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:

Input: "PPALLP"
Output: True
Example 2:

Input: "PPALLL"
Output: False

Expected Results:

1. Test Case : PPALLP
   - Result : True

2. Test Case : PPALLL
   - Result : False

"""

class Solution:
    def check_record(self, s):
        h = {'A':0, 'L':0, 'P':0}    
        for c in s:
            if c == 'L': 
                h['L'] += 1
                if h['L'] > 2: return False
            else:
                h['L'] = 0
                if c == 'A':
                    h['A'] += 1
                    if h['A'] > 1: return False
        return True


    def test(self):
        test_cases = [
            "PPALLP",
            "PPALLL"
        ] 
        for i, s in enumerate(test_cases, 1):
            print(f"\n{i}. Test Case : {s}")
            res = self.check_record(s)
            print(f"   - Result : {res}")


if __name__ == '__main__':
    Solution().test()

