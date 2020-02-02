"""
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.min = float('inf')

        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.min = min(x, self.min)
        self.nums.append((x, self.min))
        

    def pop(self):
        """
        :rtype: None
        """
        if not self.nums:
            return None
        val, _ = self.nums[-1]
        self.nums.pop()
        if self.nums:
            _, self.min = self.nums[-1]
        else:
            self.min = float('inf')
        return val

    
    def top(self):
        """
        :rtype: int
        """
        if not self.nums:
            return None
        val, _ = self.nums[-1]
        return val

    
    def getMin(self):
        """
        :rtype: int
        """
        if not self.nums:
            return None
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

