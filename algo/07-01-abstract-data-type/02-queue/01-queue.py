"""
Expected Result: 

- Is queue empty : True
- Adding 0 ~ 9 in the queue
- Queue size     : 10
- Peek           : 0
- Dequeue        : 0
- Peek           : 1
- Is queue empty : False
- Queue          : [9, 8, 7, 6, 5, 4, 3, 2, 1]

"""

class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, val):
        self.items.insert(0, val)

    def dequeue(self):
        val = self.items.pop()
        if val is not None: return val
        print("Queue is empty.")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items: return self.items[-1]
        print("Queue is empty.")

    def __repr__(self):
        return repr(self.items)


if __name__ == '__main__':
    queue = Queue()
    print(f"- Is queue empty : {queue.is_empty()}")
    print(f"- Adding 0 ~ 9 in the queue")
    for i in range(10):
        queue.enqueue(i)
    print(f"- Queue size     : {queue.size()}")
    print(f"- Peek           : {queue.peek()}")
    print(f"- Dequeue        : {queue.dequeue()}")
    print(f"- Peek           : {queue.peek()}")
    print(f"- Is queue empty : {queue.is_empty()}")
    print(f"- Queue          : {queue}")

