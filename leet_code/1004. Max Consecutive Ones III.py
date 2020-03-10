import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class CircularQueue:
    def __init__(self, size):
        self.front = 0
        self.rear = 0
        self.data = [0]*(size+1)
        self.n = size
        self.cnt = 0
    
    def is_empty(self):
        return True if self.cnt == 0 else False

    def is_full(self):
        return True if self.cnt == self.n else False
       
    def push(self, val):
        if True == self.is_full():
            return False
        self.data[self.front] = val
        self.front = (self.front+1)%self.n
        self.cnt += 1
        return True
    
    def pop(self):
        if True == self.is_empty():
            return -1
        ret = self.data[self.rear]
        self.rear = (self.rear+1)%self.n
        self.cnt -= 1
        return ret       


class Solution:
    def longestOnes(self, A, K):
        cq = CircularQueue(K+1)
        mcnt = cnt = 0
        for i, v in enumerate(A):
            if v == 0:
                cq.push(i)
                if K >= 0:
                    K -= 1

            if False == cq.is_empty() and K == -1:
                cnt = i - cq.pop() - 1
                K += 1
            
            cnt += 1
            mcnt = max(mcnt, cnt)
        return mcnt
            


stime = time.time()
#print(6 == Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
#print(10 == Solution().longestOnes_ref([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
print(10 == Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
#print(3 == Solution().longestOnes([0,0,1,1,1,0,0], 0))
print('elapse time: {} sec'.format(time.time() - stime))