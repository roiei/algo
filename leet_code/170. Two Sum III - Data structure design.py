import time
#from util_list import *
from util_tree import *


class Solution:
    def __init__(self):
        self.vals = []

    def add(self, val):
        self.vals.append(val)

    def find(self, target):
        if not self.vals:
            return False
        self.vals.sort()
        l = 0; r = len(self.vals)-1
        while l < r:
            s = self.vals[l]+self.vals[r]
            if s == target:
                return True
            if s > target:
                r -= 1
            else:   
                l += 1
        return True if s == target else False


stime = time.time()
s = Solution()
s.add(1)
s.add(3)
s.add(5)
print(s.find(4))
print(s.find(7))
print('elapse time: {} sec'.format(time.time() - stime))

