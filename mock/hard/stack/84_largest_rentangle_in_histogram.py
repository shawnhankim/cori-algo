"""
84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10

Expected Results:

0. Test Case : {'expected': 10, 'heights': [2, 1, 5, 6, 2, 3]}
   - Result 1 : 10
   - Result 2 : 10
   - Assert   : True

1. Test Case : {'expected': 4, 'heights': [2, 1, 4]}
   - Result 1 : 4
   - Result 2 : 4
   - Assert   : True

2. Test Case : {'expected': 2, 'heights': [2]}
   - Result 1 : 2
   - Result 2 : 2
   - Assert   : True

3. Test Case : {'expected': 0, 'heights': []}
   - Result 1 : 0
   - Result 2 : 0
   - Assert   : True

"""

from copy import deepcopy

class Solution:

    def largestRectangleArea1(self, heights):
        res, stk, i = 0, [], 0
        heights.append(0)

        while i < len(heights):
            if len(stk) == 0 or heights[stk[-1]] <= heights[i]:
                stk.append(i)
                i += 1
            else:
                past_idx = stk.pop()
                h = heights[past_idx]
                w = i
                if stk: w = i - stk[-1] - 1
                res = max(res, h*w)
        return res
 
    def largestRectangleArea2(self, heights):
        res, stk, heights = 0, [], [0] + heights + [0]
        for i in range(len(heights)):
            while stk and heights[stk[-1]] > heights[i]:
                j = stk.pop()
                res = max(res, (i-stk[-1]-1) * heights[j])
            stk.append(i)
        return res

    def test(self):
        test_cases = [
            { "expected": 10, "heights": [2,1,5,6,2,3] },
            { "expected":  4, "heights": [2,1,4]       },
            { "expected":  2, "heights": [2]           },
            { "expected":  0, "heights": []            }
        ]
        for i, test_case in enumerate(test_cases):
            heights, expected = test_case['heights'], test_case['expected']
            print(f"\n{i}. Test Case : {test_case}")
            res1 = self.largestRectangleArea1(deepcopy(heights))
            res2 = self.largestRectangleArea2(deepcopy(heights))
            print(f"   - Result 1 : {res1}")
            print(f"   - Result 2 : {res2}")
            print(f"   - Assert   : {expected == res1 == res2}")

if __name__ == '__main__':
    Solution().test()

