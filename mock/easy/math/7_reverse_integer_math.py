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
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Expected Results:

1. Test Case : 321
   - Result 1 of reverse integer: 123
   - Result 2 of reverse integer: 123
   - Result 3 of reverse integer: 123
   - Assert res1 == res2 == res3: True

2. Test Case : -123
   - Result 1 of reverse integer: -321
   - Result 2 of reverse integer: -321
   - Result 3 of reverse integer: -321
   - Assert res1 == res2 == res3: True

3. Test Case : 120
   - Result 1 of reverse integer: 21
   - Result 2 of reverse integer: 21
   - Result 3 of reverse integer: 21
   - Assert res1 == res2 == res3: True

4. Test Case : 21474836479
   - Result 1 of reverse integer: 0
   - Result 2 of reverse integer: 0
   - Result 3 of reverse integer: 0
   - Assert res1 == res2 == res3: True

5. Test Case : -2147483648
   - Result 1 of reverse integer: 0
   - Result 2 of reverse integer: 0
   - Result 3 of reverse integer: 0
   - Assert res1 == res2 == res3: True

6. Test Case : 2147483647
   - Result 1 of reverse integer: 0
   - Result 2 of reverse integer: 0
   - Result 3 of reverse integer: 0
   - Assert res1 == res2 == res3: True

7. Test Case : 7463847412
   - Result 1 of reverse integer: 2147483647
   - Result 2 of reverse integer: 2147483647
   - Result 3 of reverse integer: 2147483647
   - Assert res1 == res2 == res3: True

8. Test Case : -8463847412
   - Result 1 of reverse integer: -2147483648
   - Result 2 of reverse integer: -2147483648
   - Result 3 of reverse integer: -2147483648
   - Assert res1 == res2 == res3: True

9. Test Case : 0
   - Result 1 of reverse integer: 0
   - Result 2 of reverse integer: 0
   - Result 3 of reverse integer: 0
   - Assert res1 == res2 == res3: True

"""

class Solution:

    def reverse1(self, x):
        res, val = 0, abs(x)
        minv, maxv = -(2**31), (2**31)-1
        while val > 0:
            mod = val % 10
            val //= 10
            res = res*10 + mod
        if x < 0: res = -res
        return res if minv <= res <= maxv else 0
           

    def reverse2(self, x):
        sx = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        minv, maxv = -(2**31), (2**31)-1
        return 0 if minv > sx or sx > maxv else sx


    def reverse3(self, x: int) -> int:
        s = f"{abs(x)}"
        idx = len(s)
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0': idx = i
            else          : break
        s = s[:idx]
        s = s[::-1]

        if len(s) == 0: return 0
        res = int(s)
        if x < 0: res = -res
        if -(2**31) <= res <= (2**31)-1:            
            return res
        return 0


    def test(self):
        test_cases = [321, -123, 120, 21474836479, -(2**31), (2**31)-1, 7463847412, -8463847412, 0]
        for i, x in enumerate(test_cases, 1):
            print(f"\n{i}. Test Case : {x}")
            res1, res2, res3 = self.reverse1(x), self.reverse2(x), self.reverse3(x)
            print(f"   - Result 1 of reverse integer: {res1}")
            print(f"   - Result 2 of reverse integer: {res2}")
            print(f"   - Result 3 of reverse integer: {res3}")
            print(f"   - Assert res1 == res2 == res3: {res1 == res2 == res3}")


if __name__ == '__main__':
    Solution().test()



"""
321
res: 321 : -4294967296 ~ 4294967295
321
res: 321 : -4294967296 ~ 4294967295
21
res: 21 : -4294967296 ~ 4294967295
                    97463847412
res: 97463847412 : -4294967296 ~ 4294967295


123
-123
120
21474836479
0
1563847412


321
-321
21
0
0
2147483651

"""    
