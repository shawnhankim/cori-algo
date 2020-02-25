"""
Stack with min value : O(1)

Expected Results:

- Is stack empty : True
- Adding 10~1 and 1~4 into stack...
- Stack          : [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4]
- Stack size     : 14
- Peek           : 4
- Peek Min       : 1
- Pop            : 4
- Peek           : 3
- Peek Min       : 1
- Is stack empty : False
- Stack          : [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3]

"""

class MinNode(object):
    def __init__(self, val, minv):
        self.val  = val
        self.minv = minv


class Stack(object):
    def __init__(self):
        self.items = []
        self.minv = None

    def push(self, val):
        if not self.items or self.minv > val: self.minv = val
        self.items.append(MinNode(val, self.minv))

    def peek(self):
        return self.items[-1].val

    def peek_min(self):
        return self.items[-1].minv

    def pop(self):
        node = self.items.pop()
        if node:
            if node.val == self.minv:
                self.minv = self.items[-1].minv
            else: return node.val
        else:
            print("Stack is empty.")

    def is_empty(self):
        return not bool(self.items)

    def __repr__(self):
        aux = []
        for i in self.items:
            aux.append(i.val)
        return repr(aux)


if __name__ == '__main__':
    stk = Stack()
    print(f"- Is stack empty : {stk.is_empty()}")
    print( "- Adding 10~1 and 1~4 into stack...")
    for i in range(10, 0, -1):
        stk.push(i)
    for i in range(1, 5):
        stk.push(i)
    print(f"- Stack          : {stk}")

    print(f"- Stack size     : {len(stk.items)}")
    print(f"- Peek           : {stk.peek()}")
    print(f"- Peek Min       : {stk.peek_min()}")
    print(f"- Pop            : {stk.pop()}")
    print(f"- Peek           : {stk.peek()}")
    print(f"- Peek Min       : {stk.peek_min()}")
    print(f"- Is stack empty : {stk.is_empty()}")
    print(f"- Stack          : {stk}")

