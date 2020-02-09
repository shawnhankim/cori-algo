"""
997. Find the Town Judge

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N

Expected Result:

0. result: 2,  2,  2, expected: 2, N:2, trust:[[1, 2]]
1. result: 3,  3,  3, expected: 3, N:3, trust:[[1, 3], [2, 3]]
2. result:-1, -1, -1, expected:-1, N:3, trust:[[1, 3], [2, 3], [3, 1]]
3. result:-1, -1, -1, expected:-1, N:3, trust:[[1, 2], [2, 3]]
4. result: 3,  3,  3, expected: 3, N:4, trust:[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]

"""
import collections

class Solution(object):
    def find_judge1(self, N, trust):
        adj = collections.defaultdict(list)
        for v, e in trust:
            adj[v].append(e)
        in_degree = [0]*(N+1)
        for node in adj:
            for e in adj[node]:
                in_degree[e] += 1
        for i in range(1, len(in_degree)):
            if in_degree[i] == N-1 and not len(adj[i]): return i
        return -1


    def find_judge2(self, N, trust):
        in_edges, out_edges = [0]*(N+1), [0]*(N+1)
        for t in trust:
            a, b = t[0], t[1]
            in_edges[a] += 1
            out_edges[b] += 1
        for i in range(1, N+1):
            if out_edges[i] == N-1 and in_edges[i] == 0:
                return i
        return -1


    def find_judge3(self, N, trust):
        hash_in, hash_out = {}, {}
        if not trust: return N
        for t in trust:
            a, b = t[0], t[1]
            if a not in hash_in : hash_in [a]  = 1
            if b not in hash_out: hash_out[b]  = 1
            else                : hash_out[b] += 1
        for key in hash_out.keys():
            if hash_out[key] == N-1 and key not in hash_in: return key
        return -1


    def test(self):
        test_cases = [
            {"N": 2, "trust": [[1,2]]                        , "expected":  2},
            {"N": 3, "trust": [[1,3],[2,3]]                  , "expected":  3},
            {"N": 3, "trust": [[1,3],[2,3],[3,1]]            , "expected": -1},
            {"N": 3, "trust": [[1,2],[2,3]]                  , "expected": -1},
            {"N": 4, "trust": [[1,3],[1,4],[2,3],[2,4],[4,3]], "expected":  3}
        ]
        for i, test_case in enumerate(test_cases):
            n = test_case['N']
            t = test_case['trust']
            e = test_case['expected']
            res1 = self.find_judge1(n, t)
            res2 = self.find_judge2(n, t)
            res3 = self.find_judge3(n, t)
            print(f"{i}. result:{res1:2}, {res2:2}, {res3:2}, expected:{e:2}, N:{n}, trust:{t}")


if __name__ == '__main__':
    Solution().test()


