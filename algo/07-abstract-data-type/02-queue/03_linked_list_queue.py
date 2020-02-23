"""
Linked List Based Queue

Expected Results: 

- Is queue empty : True
- Adding 0 ~ 9 to queue...
- Is queue empty : False
- Linked Queue : [ 0 1 2 3 4 5 6 7 8 9 ]
- Size           : 10
- Peek           : 0
- Dequeue        : 0
- Peek           : 1
- Linked Queue : [ 1 2 3 4 5 6 7 8 9 ]

"""

class Node(object):
    def __init__(self, val=None, node=None):
        self.val  = val
        self.next = node

class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt  = 0

    def is_empty(self):
        return not bool(self.head)

    def dequeue(self):
        if self.head:
            val = self.head.val
            self.head = self.head.next
            self.cnt -= 1
            return val
        else:
            print("Queue is empty.")

    def enqueue(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            if self.tail:
                self.tail.next = node
                self.tail = node
        self.cnt += 1

    def size(self):
        return self.cnt

    def peek(self):
        return self.head.val
        
    def print(self):
        print("- Linked Queue : [", end=" ")
        node = self.head
        while node:
            print(f"{node.val}", end=" ")
            node = node.next
        print("]")


if __name__ == '__main__':
    queue = LinkedQueue()
    print(f"- Is queue empty : {queue.is_empty()}")
    print( "- Adding 0 ~ 9 to queue...")
    for i in range(10):
        queue.enqueue(i)
    print(f"- Is queue empty : {queue.is_empty()}")
    queue.print()
    print(f"- Size           : {queue.size()}")
    print(f"- Peek           : {queue.peek()}")
    print(f"- Dequeue        : {queue.dequeue()}")
    print(f"- Peek           : {queue.peek()}")
    queue.print()

