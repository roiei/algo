import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class MyCircularDeque:
    def __init__(self, k: int):
        self.n = k+1
        self.data = [0]*self.n
        self.front = 1
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull() == True:
            return False
        self.data[self.front] = value
        self.front = (self.front+1)%self.n
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull() == True:
            return False
        self.data[self.rear] = value
        self.rear = (self.rear-1)%self.n
        return True

    def deleteFront(self) -> bool:

        if self.isEmpty() == True:
            return False
        self.front = (self.front-1)%self.n
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty() == True:
            return False
        self.rear = (self.rear+1)%self.n
        return True

    def getFront(self) -> int:
        if self.isEmpty() == True:
            return -1
        return self.data[(self.front-1)%self.n]
        
    def getRear(self) -> int:
        if self.isEmpty() == True:
            return -1
        return self.data[(self.rear+1)%self.n]
        
    def isEmpty(self) -> bool:
        if ((self.front-1)%self.n) == self.rear:
            return True
        return False

    def isFull(self) -> bool:
        if self.front == self.rear:
            return True
        return False


cdq = MyCircularDeque(3)
print(True == cdq.insertLast(1))        #  // return true
print(True == cdq.insertLast(2))
print(True == cdq.insertFront(3))
print(False == cdq.insertFront(4))

print(2 == cdq.getRear())
print(True == cdq.isFull())
print(True == cdq.deleteLast())
print(True == cdq.insertFront(4))
print(4 == cdq.getFront())

