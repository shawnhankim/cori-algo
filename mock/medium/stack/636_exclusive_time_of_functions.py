"""
636. Exclusive Time of Functions

On a single threaded CPU, we execute some functions.  Each function has a unique id between 0 and N-1.

We store logs in timestamp order that describe when a function is entered or exited.

Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".  For example, "0:start:3" means the function with id 0 started at the beginning of timestamp 3.  "1:end:2" means the function with id 1 ended at the end of timestamp 2.

A function's exclusive time is the number of units of time spent in this function.  Note that this does not include any recursive calls to child functions.

The CPU is single threaded which means that only one function is being executed at a given time unit.

Return the exclusive time of each function, sorted by their function id.

 

Example 1:

 0-s  0-e 1-s         1-s 0
 <------> <-------------> <->
 +---+---+---+---+---+---+---+
 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
 +---+---+---+---+---+---+---+
 

Input:
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3, 4]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 units of time and reaches the end of time 1.
Now function 1 starts at the beginning of time 2, executes 4 units of time and ends at time 5.
Function 0 is running again at the beginning of time 6, and also ends at the end of time 6, thus executing for 1 unit of time. 
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
 

Note:

1 <= n <= 100
Two functions won't start or end at the same time.
Functions will always log when they exit.


"""

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stk, res = [], [0]*n
        for log in logs:
            s = log.split(':')
            tid, t_type, tm = int(s[0]), s[1], int(s[2])
            
            if t_type == 'start':
                stk.append([tid, tm])
            else:
                tid, stm = stk.pop()
                time_spent = tm - stm + 1
                res[tid] += time_spent
                if stk:
                    next_tid, _ = stk[-1]
                    res[next_tid] -= time_spent
        return res
    
    def exclusiveTime1(self, n: int, logs: List[str]) -> List[int]:
        res, stk, prev = [0]*n, [], None
        
        for log in logs:
            s = log.split(':')
            tid, start_or_end, tm = int(s[0]), s[1], int(s[2])
            
            if start_or_end == 'start':
                if stk:
                    stk[-1][1] += tm - prev
                stk.append([tid, 0])
            else:
                tm += 1
                res[tid] += stk[-1][1] + tm - prev
                stk.pop()
            
            prev = tm
        return res
    
"""
1
["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
2
["0:start:0","1:start:2","1:end:5","0:end:6"]

[8]
[3,4]
"""    

