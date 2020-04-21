"""
Leftmost Column with at Least a One

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.


Expected Result:
0. Test Case : [[0], [0]]
     [0]
     [0]
   - Response  : 1) -1  2) -1
   - Assertion : response 1,2 == expecttion (True)
1. Test Case : [[0], [1]]
     [0]
     [1]
   - Response  : 1) 0  2) 0
   - Assertion : response 1,2 == expecttion (True)
2. Test Case : [[0, 0], [1, 1]]
     [0, 0]
     [1, 1]
   - Response  : 1) 0  2) 0
   - Assertion : response 1,2 == expecttion (True)
3. Test Case : [[0, 0], [0, 1]]
     [0, 0]
     [0, 1]
   - Response  : 1) 1  2) 1
   - Assertion : response 1,2 == expecttion (True)
4. Test Case : [[0, 0], [0, 0]]
     [0, 0]
     [0, 0]
   - Response  : 1) -1  2) -1
   - Assertion : response 1,2 == expecttion (True)
5. Test Case : [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]]
     [0, 0, 0, 1]
     [0, 0, 1, 1]
     [0, 1, 1, 1]
   - Response  : 1) 1  2) 1
   - Assertion : response 1,2 == expecttion (True)
6. Test Case : [[1, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
     [1, 1, 1, 1, 1]
     [0, 0, 0, 1, 1]
     [0, 0, 1, 1, 1]
     [0, 0, 0, 0, 1]
     [0, 0, 0, 0, 0]
   - Response  : 1) 0  2) 0
   - Assertion : response 1,2 == expecttion (True)

"""
class BinaryMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def get(self, x, y): # x:row, y:col
        return self.matrix[x][y]

    def dimensions(self):
        n = len(self.matrix)
        m = len(self.matrix[0]) if self.matrix else 0
        return [n, m]

class Solution:
    # O(N)
    def left_most_column_with_one1(self, binaryMatrix):
        n, m = binaryMatrix.dimensions()
        res  = m
        for x in range(n-1, -1, -1):      # row
            for y in range(res-1, -1, -1):  # col
                v = binaryMatrix.get(x, y)
                if v == 1: res = min(res, y)
                elif v == 0: break
        return res if res != m else -1

    # O(N Log N)
    def left_most_column_with_one2(self, binaryMatrix):
        n, m = binaryMatrix.dimensions()
        res = m
        for x in range(n): # row
            l, r = 0, m-1
            while l <= r:  # col
                mid = (l+r) >> 1
                v = binaryMatrix.get(x, mid)
                if v == 1: r = mid-1; res = min(res, mid)
                else     : l = mid+1
        return res if res != m else -1

    def test(self):
        test_cases = [
            { "mat": [[0],[0]]                      , "expected": -1},
            { "mat": [[0],[1]]                      , "expected":  0},
            { "mat": [[0,0],[1,1]]                  , "expected":  0},
            { "mat": [[0,0],[0,1]]                  , "expected":  1},
            { "mat": [[0,0],[0,0]]                  , "expected": -1},
            { "mat": [[0,0,0,1],[0,0,1,1],[0,1,1,1]], "expected":  1},
            { "mat": [[1,1,1,1,1],[0,0,0,1,1],[0,0,1,1,1],[0,0,0,0,1],[0,0,0,0,0]], "expected": 0}
        ]
        for i, test_case in enumerate(test_cases):
            matrix, expected = test_case['mat'], test_case['expected']
            bm   = BinaryMatrix(matrix)
            res1 = self.left_most_column_with_one1(bm)
            res2 = self.left_most_column_with_one2(bm)
            print(f"{i}. Test Case : {matrix}")
            self.disp_matrix(matrix)
            print(f"   - Response  : 1) {res1}  2) {res2}")
            print(f"   - Assertion : response 1,2 == expecttion ({res1 == res2 == expected})")

    def disp_matrix(self, matrix):
        for m in matrix:
            print(f"     {m}")

if __name__ == '__main__':
    Solution().test()

