class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.n = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        self.n+= 1
        
    def pop(self):
        """
        :rtype: None
        """
        if self.n > 0:
            self.data.pop()
            self.n-= 1

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.data)


minStack = MinStack();
print(minStack.push(-2));
print(minStack.push(0));
print(minStack.push(-3))
print(minStack.getMin())   # Returns -3.
print(minStack.pop())
print(minStack.top())      # Returns 0.
print(minStack.getMin());   # Returns -2.