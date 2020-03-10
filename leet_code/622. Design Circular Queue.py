import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class MyCircularQueue:
    def __init__(self, k: int):
        self.n = k+1
        self.data = [0]*(self.n)
        self.front = 0
        self.rear = 0        

    def enQueue(self, value: int) -> bool:
        if self.isFull() == True:
            return False
        self.data[self.front] = value
        self.front = (self.front+1)%self.n
        return True        

    def deQueue(self) -> bool:
        if self.isEmpty() == True:
            return False
        self.rear = (self.rear+1)%self.n
        return True
        
    def Front(self) -> int:
        if self.isEmpty() == True:
            return -1
        return self.data[self.rear]        

    def Rear(self) -> int:
        if self.isEmpty() == True:
            return -1
        return self.data[self.front - 1]        

    def isEmpty(self) -> bool:
        if self.front == self.rear:
            return True
        return False        

    def isFull(self) -> bool:
        if (self.front+1)%self.n == self.rear:
            return True
        return False


circularQueue = MyCircularQueue(3)
print(True == circularQueue.enQueue(1))        #  // return true
print(True == circularQueue.enQueue(2))        #  // return true
print(True == circularQueue.enQueue(3))        #  // return true
print(False == circularQueue.enQueue(4))        #  // return false, the queue is full
print(3 == circularQueue.Rear())       # // return 3
print(True == circularQueue.isFull())     # // return true
print(True == circularQueue.deQueue())        # // return true
print(True == circularQueue.enQueue(4))        #  // return true
print(4 == circularQueue.Rear())       # // return 4