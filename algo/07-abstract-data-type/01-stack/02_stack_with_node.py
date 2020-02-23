"""
Expected Result:

- Is stack empty : True
- Adding 0 ~ 9 in stack
- Stack          : [ 9  8  7  6  5  4  3  2  1  0  ]
- Stack size     : 10
- Peek           : 9
- Pop            : 9
- Peek           : 8
- Is stack empty : False
- Stack          : [ 8  7  6  5  4  3  2  1  0  ]

"""

class Node(object):
    def __init__(self, val=None, next=None):
        self.val  = val
        self.next = next 

class Stack(object):
    def __init__(self):
        self.head = None
        self.cnt  = 0

    def is_empty(self):
        return not bool(self.head)

    def push(self, val):
        self.head = Node(val, self.head)
        self.cnt += 1
            
    def pop(self):
        if self.cnt > 0 and self.head:
            node = self.head
            self.head = node.next
            self.cnt -= 1
            return node.val
        print("Stack is empty")

    def peek(self):
        if self.cnt > 0 and self.head:
            return self.head.val
        print("Stack is empty")

    def size(self):
        return self.cnt

    def print_list(self):
        node = self.head
        print("- Stack          : [", end=" ")
        while node:
            print(f"{node.val} ", end=" ")
            node = node.next
        print("]")

if __name__ == "__main__":
    stack = Stack()
    print(f"- Is stack empty : {stack.is_empty()}")
    print(f"- Adding 0 ~ 9 in stack")
    for i in range(10):
        stack.push(i)
    stack.print_list()
    print(f"- Stack size     : {stack.size()}")
    print(f"- Peek           : {stack.peek()}")
    print(f"- Pop            : {stack.pop()}")
    print(f"- Peek           : {stack.peek()}")
    print(f"- Is stack empty : {stack.is_empty()}")
    stack.print_list()



