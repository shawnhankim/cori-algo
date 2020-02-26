"""
Set of Stacks : in case the capacity of stack exceeds

Expected Results:
- Is stack empty : True
- Adding 0~9 to stack...
- Stack          : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  * size(10) = len of set stacks(1) * capacity(5) + size(5)
- Size           : 10
- Peek           : 9
- Pop            : 9
- Peek           : 8
- Is stack empty : False
  * size(9) = len of set stacks(1) * capacity(5) + size(4)
- Size           : 9
- Stack          : [0, 1, 2, 3, 4, 5, 6, 7, 8]
  * size(8) = len of set stacks(1) * capacity(5) + size(3)
  * Pop -> Stack Size & Stack : 8 ->  8 [0, 1, 2, 3, 4, 5, 6, 7]
  * size(7) = len of set stacks(1) * capacity(5) + size(2)
  * Pop -> Stack Size & Stack : 7 ->  7 [0, 1, 2, 3, 4, 5, 6]
  * size(6) = len of set stacks(1) * capacity(5) + size(1)
  * Pop -> Stack Size & Stack : 6 ->  6 [0, 1, 2, 3, 4, 5]
  * size(5) = len of set stacks(0) * capacity(5) + size(5)
  * Pop -> Stack Size & Stack : 5 ->  5 [0, 1, 2, 3, 4]
  * size(4) = len of set stacks(0) * capacity(5) + size(4)
  * Pop -> Stack Size & Stack : 4 ->  4 [0, 1, 2, 3]
  * size(3) = len of set stacks(0) * capacity(5) + size(3)
  * Pop -> Stack Size & Stack : 3 ->  3 [0, 1, 2]
  * size(2) = len of set stacks(0) * capacity(5) + size(2)
  * Pop -> Stack Size & Stack : 2 ->  2 [0, 1]
  * size(1) = len of set stacks(0) * capacity(5) + size(1)
  * Pop -> Stack Size & Stack : 1 ->  1 [0]
  * size(0) = len of set stacks(0) * capacity(5) + size(0)
  * Pop -> Stack Size & Stack : 0 ->  0 []

"""

class Stack(object):
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not bool(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        item = self.items.pop()
        if item is not None: return item
        print("Stack is empty.")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items: return self.items[-1]
        print("Stack is empty.")

    def __repr__(self):
        return repr(self.items)


class SetOfStacks(Stack):
    def __init__(self, capacity=4):
        self.set_stacks, self.items, self.capacity = [], [], capacity

    def push(self, item):
        if self.size() >= self.capacity:
            self.set_stacks.append(self.items)
            self.items = []
        self.items.append(item)

    def pop(self):
        item = self.items.pop()
        if self.is_empty() and self.set_stacks:
            self.items = self.set_stacks.pop()
        return item

    def stack_size(self):
        a = len(self.set_stacks) 
        b = a * self.capacity
        c = self.size()
        d = a*b + c
        print(f"  * size({d}) = len of set stacks({a}) * capacity({self.capacity}) + size({c})")
        return len(self.set_stacks) * self.capacity + self.size()
      
    def __repr__(self):
        aux = []
        for s in self.set_stacks:
            aux.extend(s)
        aux.extend(self.items)
        return repr(aux)


if __name__ == '__main__':  
    stk = SetOfStacks(capacity=5)
    print(f"- Is stack empty : {stk.is_empty()}")
    print( "- Adding 0~9 to stack...")
    for i in range(10):
        stk.push(i)
    print(f"- Stack          : {stk}")
    print(f"- Size           : {stk.stack_size()}")
    print(f"- Peek           : {stk.peek()}")
    print(f"- Pop            : {stk.pop()}")
    print(f"- Peek           : {stk.peek()}")
    print(f"- Is stack empty : {stk.is_empty()}")
    print(f"- Size           : {stk.stack_size()}")
    print(f"- Stack          : {stk}")
    for i in range(8, -1, -1):
        print(f"  * Pop -> Stack Size & Stack : {stk.pop()} -> {stk.stack_size():2} {stk}")

