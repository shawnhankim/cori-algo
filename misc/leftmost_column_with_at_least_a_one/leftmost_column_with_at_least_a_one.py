
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
    def left_most_column_with_one(self, binaryMatrix):
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
            bm  = BinaryMatrix(matrix)
            res = self.left_most_column_with_one(bm)
            print(f"{i}. Test Case : {matrix}")
            self.disp_matrix(matrix)
            print(f"   - Response  : {res}")
            print(f"   - Assertion : response == expecttion ({res == expected})")

    def disp_matrix(self, matrix):
        for m in matrix:
            print(f"     {m}")

if __name__ == '__main__':
    Solution().test()

