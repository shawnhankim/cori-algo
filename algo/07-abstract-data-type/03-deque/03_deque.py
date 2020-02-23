"""
Deque : Combination of queue and stack

Expected Result

- Is deque empty : True
- Adding 0 ~ 9 to deque...
- Deque size     : 10
- Peek           : 0
- Dequeue        : 0
- Peek           : 1
- Is deque empty : False

- Deque          : [9, 8, 7, 6, 5, 4, 3, 2, 1]
- dequeue_front(): 9
- Peek           : 1
- Deque          : [8, 7, 6, 5, 4, 3, 2, 1]
- enqueue_back(A)...
- Peek           : A
- Deque          : [8, 7, 6, 5, 4, 3, 2, 1, 'A']

"""

class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        val = self.items.pop()
        if val is not None: return val
        print("Queue is empty")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items: return self.items[-1]
        print("Queue is empty")

    def __repr__(self):
        return repr(self.items)


class Deque(Queue):
    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self):
        val = self.items.pop(0)
        if val is not None: return val
        print("Deque is empty.")


if __name__ == '__main__':
    deque = Deque()
    print(f"- Is deque empty : {deque.is_empty()}")
    print( "- Adding 0 ~ 9 to deque...")
    for i in range(10):
        deque.enqueue(i)
    print(f"- Deque size     : {deque.size()}")
    print(f"- Peek           : {deque.peek()}")
    print(f"- Dequeue        : {deque.dequeue()}")
    print(f"- Peek           : {deque.peek()}")
    print(f"- Is deque empty : {deque.is_empty()}")
    print()
    print(f"- Deque          : {deque}")
    print(f"- dequeue_front(): {deque.dequeue_front()}")
    print(f"- Peek           : {deque.peek()}")
    print(f"- Deque          : {deque}")
    print(f"- enqueue_back(A)...")
    deque.enqueue_back('A')
    print(f"- Peek           : {deque.peek()}")
    print(f"- Deque          : {deque}")

