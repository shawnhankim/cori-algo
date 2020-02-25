"""
collections package : deque

Expected Results : 

make deque      : deque(['a', 'b', 'c'])
q.append('d')   : deque(['a', 'b', 'c', 'd'])
q.popleft()     : a -> deque(['b', 'c', 'd'])
q.pop()         : d -> deque(['b', 'c'])
appendleft('e') : deque(['e', 'b', 'c'])
q.rotate(1)     : deque(['c', 'e', 'b'])
q.rotate(2)     : deque(['e', 'b', 'c'])
q.rotate(3)     : deque(['e', 'b', 'c'])
q.rotate(4)     : deque(['c', 'e', 'b'])
q.rotate(-1)    : deque(['e', 'b', 'c'])
q.rotate(-2)    : deque(['c', 'e', 'b'])

"""

from collections import deque

q = deque(['a', 'b', 'c'])
print(f"make deque      : {q}")

q.append('d')
print(f"q.append('d')   : {q}")

a = q.popleft()
print(f"q.popleft()     : {a} -> {q}")

b = q.pop()
print(f"q.pop()         : {b} -> {q}")

q.appendleft('e')
print(f"appendleft('e') : {q}")

q.rotate(1)
print(f"q.rotate(1)     : {q}")

q.rotate(2)
print(f"q.rotate(2)     : {q}")

q.rotate(3)
print(f"q.rotate(3)     : {q}")

q.rotate(4)
print(f"q.rotate(4)     : {q}")

q.rotate(-1)
print(f"q.rotate(-1)    : {q}")

q.rotate(-2)
print(f"q.rotate(-2)    : {q}")

