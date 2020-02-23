"""
Expected Result:

- Is stack empty : True
- Adding 0~9 in stack
- Size of stack  : 10
- Peek           : 9
- Pop            : 9
- Peek           : 8
- Is stack empty : False
- Stack          : [0, 1, 2, 3, 4, 5, 6, 7, 8]

"""

class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if value: return value
        print("Stack is empty.")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items: return self.items[-1]
        print("Stack is empty.")

    def __repr__(self):
        return repr(self.items)

if __name__ == "__main__":
    stack = Stack()
    print(f"- Is stack empty : {stack.is_empty()}")
    print( "- Adding 0~9 in stack")
    for i in range(10):
        stack.push(i)
    print(f"- Size of stack  : {stack.size()}")
    print(f"- Peek           : {stack.peek()}")
    print(f"- Pop            : {stack.pop()}")
    print(f"- Peek           : {stack.peek()}")
    print(f"- Is stack empty : {stack.is_empty()}")
    print(f"- Stack          : {stack}")

