import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class CircularQueue:
    def __init__(self, k):
        self.n = k
        self.data = [0]*self.n
        self.front = 0
        self.rear = self.n-1

    def is_empty(self):
        if self.front == (self.rear+1)%self.n:
            return True
        return False

    def is_full(self):
        if self.front == self.rear:
            return True
        return False

    def insert(self, val):
        if True == self.is_full():
            return False
        self.data[self.front] = val
        self.front = (self.front+1)%self.n
        return True

    def get(self):
        if True == self.is_empty():
            return None
        idx = (self.rear+1)%self.n
        ret = self.data[idx]
        self.rear = idx
        return ret

class Solution:
    def findMaxAverage_timeout(self, nums: [int], k: int) -> float:
        n = len(nums)
        if n < k:
            return sum(nums)/k
        mavg = float('-inf')
        wnd = []
        for i in range(n):
            if len(wnd) == k:
                wnd.pop(0)
            wnd += nums[i],
            mavg = max(mavg, sum(wnd)/k)
        return mavg

    def findMaxAverage_sliding_wnd(self, nums: [int], k: int) -> float:
        n = len(nums)
        if n < k:
            return sum(nums)/k
        mavg = float('-inf')
        tot = 0
        cq = CircularQueue(k+1)
        for i in range(n):
            if True == cq.is_full():
                tot -= cq.get()
            tot += nums[i]
            cq.insert(nums[i])
            if True == cq.is_full():
                mavg = max(mavg, tot)
        return mavg/k

    def findMaxAverage(self, nums: [int], k: int) -> float:
        n = len(nums)
        tot = 0
        for i in range(k):
            tot += nums[i]
        mval = tot
        for i in range(k, n):
            tot += nums[i]-nums[i-k]
            mval = max(mval, tot)
        return mval/k


# cq = CircularQueue(4+1)
# vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for val in vals:
#     if True == cq.is_full():
#         print('get = ', cq.get())
#     cq.insert(val)
#     print(cq.data)

stime = time.time()
print(-1 == Solution().findMaxAverage([5], 1))
#print( Solution().findMaxAverage([-6662,5432,-8558,-8935,8731,-3083,4115,9931,-4006,-3284,-3024,1714,-2825,-2374,-2750,-959,6516,9356,8040,-2169,-9490,-3068,6299,7823,-9767,5751,-7897,6680,-1293,-3486,-6785,6337,-9158,-4183,6240,-2846,-2588,-5458,-9576,-1501,-908,-5477,7596,-8863,-4088,7922,8231,-4928,7636,-3994,-243,-1327,8425,-3468,-4218,-364,4257,5690,1035,6217,8880,4127,-6299,-1831,2854,-4498,-6983,-677,2216,-1938,3348,4099,3591,9076,942,4571,-4200,7271,-6920,-1886,662,7844,3658,-6562,-2106,-296,-3280,8909,-8352,-9413,3513,1352,-8825], 90))
# print(12.75 == Solution().findMaxAverage([1,12,-5,-6,50,3], 4))
# print(-1 == Solution().findMaxAverage([-1], 1))
print('elapse time: {} sec'.format(time.time() - stime))