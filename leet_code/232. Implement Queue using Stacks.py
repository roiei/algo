
import time


class MyQueue:
    def __init__(self):
        self.tstk = []
        self.pstk = []

    def push(self, x: int) -> None:
        while self.pstk:
            self.tstk.append(self.pstk.pop())
        self.pstk.append(x)
        while self.tstk:
            self.pstk.append(self.tstk.pop())

    def pop(self) -> int:
        if not self.pstk:
            return -1
        return self.pstk.pop()

    def peek(self) -> int:
        if not self.pstk:
            return -1
        return self.pstk[-1]

    def empty(self) -> bool:
        return True if not self.pstk else False

queue = MyQueue();

queue.push(1);
queue.push(2);  
print(queue.peek())  # returns 1
print(queue.pop())   # returns 1
print(queue.empty()) # returns false
