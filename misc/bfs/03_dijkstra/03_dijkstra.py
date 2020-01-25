"""
Dijkstra Algorithm

           5              4             3
   AAA ---------> BBB --------> CCC ---------> DDD
     \             A \           |              A
      \            |   \ 2       |6             |
       \           |8    \       |            1 /
        \          |       \     V             /
         +------> EEE --------> FFF ----------+ 
            2            7
"""

from collections import deque

class Solution(object):
    def dijkstra(self, paths, start, end):
    
        # Initialize table : parent, weight, visited
        tbl = {}
        for node in paths.keys():
            tbl[node] = {}
            tbl[node]['p'] = None
            tbl[node]['w'] = float('inf')
            tbl[node]['v'] = False
        tbl[start]['p'] = 'root'
        tbl[start]['w'] = 0

        # Boundary check
        if start == end:
            return tbl, 0

        # Search shortest weight based path
        q = deque()
        q.append(start)
        while q:
            node = q.popleft()
            if tbl[node]['v']:
                continue
            if node == end:
                break
            node_weight = tbl[node]['w']
            for adj in paths[node].keys():
                adj_weight = node_weight + paths[node][adj]
                if tbl[adj]['w'] > adj_weight:
                   tbl[adj]['w'] = adj_weight
                   tbl[adj]['p'] = node
                q.append(adj)
            tbl[node]['v'] = True

        return tbl, tbl[end]['w']

    def print_shortest_path(self, table, start, end):
        q = deque()
        node = end
        q.append(node)
        while node != start:
            if not table[node]['p']:
                print("   - no paths")
                return
            node = table[node]['p']
            q.append(node)
        str = ""
        while q:
            node = q.pop()
            str += f"{node}" if node == end else f"{node} -> "
        print(f"   - paths  : {str}")               

    def test(self):
        
        paths = {
            "AAA": {"BBB": 5, "EEE": 4},
            "BBB": {"CCC": 4, "FFF": 2},
            "CCC": {"DDD": 3, "FFF": 6},
            "DDD": {},
            "EEE": {"BBB": 8, "FFF": 7},
            "FFF": {"DDD": 1}
        }

        test_cases = [
            {"start": "AAA", "end": "DDD"},
            {"start": "BBB", "end": "DDD"},
            {"start": "DDD", "end": "AAA"},
            {"start": "EEE", "end": "DDD"}
        ]

        for i, test_case in enumerate(test_cases, 1):
            start  = test_case['start']
            end    = test_case['end']
            tbl, weight = self.dijkstra(paths, start, end)
            print(f"\n{i}. shortest path from {start} to {end}") 
            print(f"   - weight : {weight}")
            self.print_shortest_path(tbl, start, end)
        print()


Solution().test()
