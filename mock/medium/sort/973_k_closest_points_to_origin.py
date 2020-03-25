"""
973. K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000

Expected Results:

1. Test Case : {'K': 1, 'points': [[1, 3], [-2, 2]]}
   - Result 1 : [[-2, 2]]
   - Result 2 : [[-2, 2]]
   - Result 3 : [[-2, 2]]
   - Result 5 : [[-2, 2]]

2. Test Case : {'K': 2, 'points': [[3, 3], [5, -1], [-2, 4]]}
   - Result 1 : [[-2, 4], [3, 3]]
   - Result 2 : [[-2, 4], [3, 3]]
   - Result 3 : [[3, 3], [-2, 4]]
   - Result 5 : [[3, 3], [-2, 4]]

3. Test Case : {'K': 2, 'points': [[0, 1], [1, 0]]}
   - Result 1 : [[0, 1], [1, 0]]
   - Result 2 : [[0, 1], [1, 0]]
   - Result 3 : [[0, 1], [1, 0]]
   - Result 5 : [[0, 1], [1, 0]]
"""

from heapq import heappop, heappush
from collections import defaultdict

class Solution:

    def kClosest1(self, points, K):
        pq = []
        for p in points:
            d = p[0]**2 + p[1]**2
            heappush(pq, (-d, p))
            if len(pq) == (K+1): heappop(pq)
        res = []
        for _, p in pq:
            res.append(p)
        return res


    def kClosest2(self, points, K):
        pq = []
        for p in points:
            heappush(pq, (-p[0]**2 - p[1]**2, p))
            if len(pq) == K+1: heappop(pq)
        res = map(lambda x: x[1], pq)
        return list(res)


    def kClosest3(self, points, K):

        pq = []
        hs = defaultdict(list)
        for i, point in enumerate(points):
            x, y = point[0], point[1]
            d = x**2 + y**2
            heappush(pq, d)
            hs[d].append(i)
        
        res, cnt = [], 0
        for j in range(K):
            d = heappop(pq)
            for i in hs[d]:
                res.append(points[i])
                if len(res) == K: return res
            
        return res


    def kClosest5(self, points, K):
        points.sort(key = lambda x: x[0]**2 + x[1]**2)
        return points[:K]

       
    def test(self):
        test_cases = [
            { "K": 1,
              "points": [[1,3],[-2,2]]
            },
            { "K": 2,
              "points": [[3,3],[5,-1],[-2,4]]
            },
            { "K": 2,
              "points": [[0,1],[1,0]]
            }
        ]
        for i, test_case in enumerate(test_cases, 1):
            print(f"\n{i}. Test Case : {test_case}")
            K, points = test_case['K'], test_case['points']
            res1 = self.kClosest1(points, K)
            res2 = self.kClosest2(points, K)
            res3 = self.kClosest3(points, K)
            res5 = self.kClosest5(points, K)
            print(f"   - Result 1 : {res1}")
            print(f"   - Result 2 : {res2}")
            print(f"   - Result 3 : {res3}")
            print(f"   - Result 5 : {res5}")


if __name__ == '__main__':
    Solution().test()


