"""
836. Rectangle Overlap

A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Notes:

Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.


"""

class Solution:

    def isRectangleOverlap1(self, r1, r2):
        x1, y1, x2, y2 = range(4)
        return not (r1[y2] <= r2[y1] or r1[x2] <= r2[x1] or r1[y1] >= r2[y2] or r1[x1] >= r2[x2])

    def isRectangleOverlap2(self, r1: List[int], r2: List[int]) -> bool:
        x1, y1, x2, y2 = range(4)
        if r1[y2] <= r2[y1]: return False
        if r1[x2] <= r2[x1]: return False
        if r1[y1] >= r2[y2]: return False
        if r1[x1] >= r2[x2]: return False
        return True

    
"""
[0,0,2,2]
[1,1,3,3]
[0,0,1,1]
[1,0,2,1]
[7,8,13,15]
[10,8,12,20]
[2,17,6,20]
[3,8,6,20]
"""
