"""
743. Network Delay Time

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Example 1:

        1
  (2) -----> (1)
   |
   |    1           1
   +-------> (3) -------> (4)


Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2


Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

Expected Results:

1. Test Case: {'N': 4, 'K': 2, 'expectation': 2, 'times': [[2, 1, 1], [2, 3, 1], [3, 4, 1]]}
   - Graph of Travel Times w/ min heap
     +------+----------------+--------------------+
     | node | adjacent nodes | network delay time |
     +------+----------------+--------------------+
     |    1 |                |                  1 |
     |    2 | 1, 3           |                  0 |
     |    3 | 4              |                  1 |
     |    4 |                |                  2 |
     +------+----------------+--------------------+
   - Graph of Travel Times w/ Queue
     +------+----------------+---------+--------------------+
     | node | adjacent nodes | visited | network delay time |
     +------+----------------+---------+--------------------+
     |    1 |                |       1 |                  1 |
     |    2 | 1, 3           |       1 |                  0 |
     |    3 | 4              |       1 |                  1 |
     |    4 |                |       1 |                  2 |
     +------+----------------+---------+--------------------+
   - Result of network delay time w/ heap    : 2
   - Result of network delay time w/ queue   : 2
   - Assert expectation == result1 == result2: True

2. Test Case: {'N': 2, 'K': 2, 'expectation': -1, 'times': [[1, 2, 1]]}
   - Graph of Travel Times w/ min heap
     +------+----------------+--------------------+
     | node | adjacent nodes | network delay time |
     +------+----------------+--------------------+
     |    1 | 2              |                inf |
     |    2 |                |                  0 |
     +------+----------------+--------------------+
   - Graph of Travel Times w/ Queue
     +------+----------------+---------+--------------------+
     | node | adjacent nodes | visited | network delay time |
     +------+----------------+---------+--------------------+
     |    1 | 2              |       0 |                inf |
     |    2 |                |       1 |                  0 |
     +------+----------------+---------+--------------------+
   - Result of network delay time w/ heap    : -1
   - Result of network delay time w/ queue   : -1
   - Assert expectation == result1 == result2: True

3. Test Case: {'N': 2, 'K': 2, 'expectation': 3, 'times': [[1, 2, 1], [2, 1, 3]]}
   - Graph of Travel Times w/ min heap
     +------+----------------+--------------------+
     | node | adjacent nodes | network delay time |
     +------+----------------+--------------------+
     |    1 | 2              |                  3 |
     |    2 | 1              |                  0 |
     +------+----------------+--------------------+
   - Graph of Travel Times w/ Queue
     +------+----------------+---------+--------------------+
     | node | adjacent nodes | visited | network delay time |
     +------+----------------+---------+--------------------+
     |    1 | 2              |       1 |                  3 |
     |    2 | 1              |       1 |                  0 |
     +------+----------------+---------+--------------------+
   - Result of network delay time w/ heap    : 3
   - Result of network delay time w/ queue   : 3
   - Assert expectation == result1 == result2: True

4. Test Case: {'N': 3, 'K': 2, 'expectation': 2, 'times': [[2, 1, 1], [1, 3, 1], [3, 1, 1]]}
   - Graph of Travel Times w/ min heap
     +------+----------------+--------------------+
     | node | adjacent nodes | network delay time |
     +------+----------------+--------------------+
     |    1 | 3              |                  1 |
     |    2 | 1              |                  0 |
     |    3 | 1              |                  2 |
     +------+----------------+--------------------+
   - Graph of Travel Times w/ Queue
     +------+----------------+---------+--------------------+
     | node | adjacent nodes | visited | network delay time |
     +------+----------------+---------+--------------------+
     |    1 | 3              |       1 |                  1 |
     |    2 | 1              |       1 |                  0 |
     |    3 | 1              |       1 |                  2 |
     +------+----------------+---------+--------------------+
   - Result of network delay time w/ heap    : 2
   - Result of network delay time w/ queue   : 2
   - Assert expectation == result1 == result2: True

5. Test Case: {'N': 3, 'K': 1, 'expectation': 2, 'times': [[1, 2, 1], [2, 3, 2], [1, 3, 2]]}
   - Graph of Travel Times w/ min heap
     +------+----------------+--------------------+
     | node | adjacent nodes | network delay time |
     +------+----------------+--------------------+
     |    1 | 2, 3           |                  0 |
     |    2 | 3              |                  1 |
     |    3 |                |                  2 |
     +------+----------------+--------------------+
   - Graph of Travel Times w/ Queue
     +------+----------------+---------+--------------------+
     | node | adjacent nodes | visited | network delay time |
     +------+----------------+---------+--------------------+
     |    1 | 2, 3           |       1 |                  0 |
     |    2 | 3              |       1 |                  1 |
     |    3 |                |       1 |                  2 |
     +------+----------------+---------+--------------------+
   - Result of network delay time w/ heap    : 2
   - Result of network delay time w/ queue   : 2
   - Assert expectation == result1 == result2: True

6. Test Case: {'N': 3, 'K': 1, 'expectation': 3, 'times': [[1, 2, 1], [2, 3, 2], [1, 3, 4]]}
   - Graph of Travel Times w/ min heap
     +------+----------------+--------------------+
     | node | adjacent nodes | network delay time |
     +------+----------------+--------------------+
     |    1 | 2, 3           |                  0 |
     |    2 | 3              |                  1 |
     |    3 |                |                  3 |
     +------+----------------+--------------------+
   - Graph of Travel Times w/ Queue
     +------+----------------+---------+--------------------+
     | node | adjacent nodes | visited | network delay time |
     +------+----------------+---------+--------------------+
     |    1 | 2, 3           |       1 |                  0 |
     |    2 | 3              |       1 |                  1 |
     |    3 |                |       1 |                  3 |
     +------+----------------+---------+--------------------+
   - Result of network delay time w/ heap    : 3
   - Result of network delay time w/ queue   : 3
   - Assert expectation == result1 == result2: True

7. Test Case: {'N': 4, 'K': 1, 'expectation': -1, 'times': [[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]]}
   - Graph of Travel Times w/ min heap
     +------+----------------+--------------------+
     | node | adjacent nodes | network delay time |
     +------+----------------+--------------------+
     |    1 | 2, 3           |                  0 |
     |    2 | 3, 1           |                  1 |
     |    3 |                |                  4 |
     |    4 |                |                inf |
     +------+----------------+--------------------+
   - Graph of Travel Times w/ Queue
     +------+----------------+---------+--------------------+
     | node | adjacent nodes | visited | network delay time |
     +------+----------------+---------+--------------------+
     |    1 | 2, 3           |       1 |                  0 |
     |    2 | 3, 1           |       1 |                  1 |
     |    3 |                |       1 |                  4 |
     |    4 |                |       0 |                inf |
     +------+----------------+---------+--------------------+
   - Result of network delay time w/ heap    : -1
   - Result of network delay time w/ queue   : -1
   - Assert expectation == result1 == result2: True

"""

import heapq
from collections import defaultdict

class Solution:
    def network_delay_time2(self, times, N, K):
        # Create graph
        g, q, dist, visited = {}, [], {}, {}
        for u, v, w in times:
            if u not in g: g[u] = {}
            if v not in g: g[v] = {}
            g[u][v] = w
            dist[u] = dist[v] = float('inf')
            visited[u] = visited[v] = False
        dist[K] = 0

        # Algorithm
        res = -1
        q.append(K)
        while q:
            u = q.pop()
            if visited[u]: continue
            if u not in g:
                visited[u] = True
                continue

            for v in g[u].keys():
                w = g[u][v]
                d = dist[u] + w
                dist[v] = min(dist[v], d) 
                q.append(v)
            visited[u] = True

        self.print_graph(g, dist, visited)
        for u in visited.keys():
            if not visited[u]: return -1
        for d in dist.keys():
            res = max(res, dist[d])
        return res
 
    def network_delay_time_heap(self, times, N, K):
        pq = [(0, K)]
        g, dist = defaultdict(dict), [float('inf')] * (N+1)
        for u, v, w in times:
            g[u][v] = w
        dist[K] = 0

        while pq:
            cur_d, u = heapq.heappop(pq)
            for v in g[u]:
                w = g[u][v]
                d = cur_d + w
                if dist[v] > d:
                    dist[v] = d
                    heapq.heappush(pq, (d, v))
        res = max(dist[1:])
        self.print_graph_heap(g, dist, N)
        return -1 if res == float('inf') else res


    def print_graph_heap(self, graph, distance, N):
        print( "   - Graph of Travel Times w/ min heap")
        print( "     +------+----------------+--------------------+")
        print( "     | node | adjacent nodes | network delay time |")
        print( "     +------+----------------+--------------------+")

        for u in range(1, N+1):
            adj = self.adjacent_str(graph[u])
            print(f"     | {u:4} | {adj:14} | {distance[u]:18} |")
        print( "     +------+----------------+--------------------+")


    def network_delay_time_queue(self, times, N, K):
        # Create graph
        visited = [False] * (N+1)
        dist    = [float('inf')] * (N+1)
        dist[K] = 0
        graph   = defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w

        # Algorithm
        q = [K]
        while q:
            u = q.pop()
            if visited[u]: continue

            for v in graph[u]:
                d = dist[u] + graph[u][v]
                if dist[v] > d:
                    dist[v] = d
                    q.append(v)
            visited[u] = True

        self.print_graph_queue(graph, dist, visited, N)
        res = max(dist[1:])
        return -1 if res == float('inf') else res


    def print_graph_queue(self, graph, distance, visited, N):
        print( "   - Graph of Travel Times w/ Queue")
        print( "     +------+----------------+---------+--------------------+")
        print( "     | node | adjacent nodes | visited | network delay time |")
        print( "     +------+----------------+---------+--------------------+")

        for u in range(1, N+1):
            adj = self.adjacent_str(graph[u])
            print(f"     | {u:4} | {adj:14} | {visited[u]:7} | {distance[u]:18} |")
        print( "     +------+----------------+---------+--------------------+")


    def adjacent_str(self, graph):
        adj_list = []
        if graph:
            for v in graph.keys():
                adj_list.append(f"{v}")
        return ", ".join(adj_list)


    def test(self):
        test_cases = [
            {"N":4, "K":2, "expectation": 2, "times":[[2,1,1],[2,3,1],[3,4,1]]},
            {"N":2, "K":2, "expectation":-1, "times":[[1,2,1]]},
            {"N":2, "K":2, "expectation": 3, "times":[[1,2,1],[2,1,3]]},
            {"N":3, "K":2, "expectation": 2, "times":[[2,1,1],[1,3,1],[3,1,1]]},
            {"N":3, "K":1, "expectation": 2, "times":[[1,2,1],[2,3,2],[1,3,2]]},
            {"N":3, "K":1, "expectation": 3, "times":[[1,2,1],[2,3,2],[1,3,4]]},
            {"N":4, "K":1, "expectation":-1, "times":[[1,2,1],[2,3,7],[1,3,4],[2,1,2]]}
        ]
        for i, test_case in enumerate(test_cases, 1):
            N, K, times = test_case['N'], test_case['K'], test_case['times']
            expectation = test_case['expectation']
            print(f"\n{i}. Test Case: {test_case}")
            res1 = self.network_delay_time_heap(times, N, K)
            res2 = self.network_delay_time_queue(times, N, K)
            print(f"   - Result of network delay time w/ heap    : {res1}")
            print(f"   - Result of network delay time w/ queue   : {res2}")
            print(f"   - Assert expectation == result1 == result2: {res1 == res2 == expectation}")


if __name__ == '__main__':
    Solution().test()

