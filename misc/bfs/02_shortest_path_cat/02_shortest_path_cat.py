"""
Find the shortest path from "CAB" to "BAT"
 
            MAT ------+
             A        |
             |        V
            CAT ---> BAT (End)
             A        A
             |        |
  CAB ----> CAR ---> BAR
(Start)
"""

from collections import deque

class Solution(object):

    def find_shortest_path(self, paths, start, end):
        """
        graph : set of paths
        start : name of start path
        end   : name of end path
        return: table, shortest paths

        approach

        - data structure       space  time
          (1) data graph : set O(V+E) O(V+E)
          (2) table      : set O(E)   
              node  parent  dist  visited
        - logic
          - boundary check
            - check if start is end
          - declare queue : q = list()
          - initialize table (tbl)
            - node  parent  dist  visited
              start root    inf   false
                :   none    inf   false
          - set first queue
            - q.append(start)
          - while q:
                node = pop queue
                if tbl[node][visited]
                    continue
                dist = tbl[node][dist]
                for adj in graph[node].items():
                    if tbl[adj][dist] > dist
                       tbl[adj][dist] = dist + 1
                       tbl[adj][parent] = node
                    q : add (adj)
                tbl[node][visited] = True
          - return tbl, tbl[end][dist]
        """ 
        if paths[start] == paths[end]:
            return None, 0

        q = deque()
        t = {}
    
        for path in paths.keys():
            t[path] = {}
            t[path]['parent' ] = ""
            t[path]['dist'   ] = float('inf')
            t[path]['visited'] = False

        t[start]['parent'] = 'Root'
        t[start]['dist'  ] = 0
        q.append(start)
        while q:
            node = q.popleft()
            if t[node]['visited']:
                continue
            if node == end:
                break
            dist = t[node]['dist']
            for adj in paths[node]:
                if  t[adj]['dist'] > dist:
                    t[adj]['dist'] = dist + 1
                    t[adj]['parent'] = node
                q.append(adj)
            t[node]['visited'] = True

        return t, t[end]['dist']

paths = {
    "CAB": ["CAR", "CAT"],
    "CAR": ["CAT", "BAR"],
    "CAT": ["MAT", "BAT"],
    "MAT": ["BAT"],
    "BAT": [],
    "BAR": ["BAT"]
}

test_cases = [
    {"start": "CAB", "end": "CAR"},
    {"start": "CAB", "end": "CAT"},
    {"start": "CAB", "end": "BAT"}
]

for i, test_case in enumerate(test_cases, 1):
    t, shortest_path = Solution().find_shortest_path(paths, test_case['start'], test_case['end'])
    print(f"\n{i}. Shortest distance from {test_case['start']} to {test_case['end']} = {shortest_path}")
    stack = []
    path  = test_case['end']
    stack.append(path)
    while path:
       path = t[path]['parent']
       if path == 'Root':
           break
       stack.append(path) 
    str = ""      
    while stack:
       path = stack.pop()
       str += f"{path} -> "
    str += "*** YEAH ***"
    print(f"            path : {str}")
print()
