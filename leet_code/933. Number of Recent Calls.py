import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class RecentCounter:

    def __init__(self):
        self.pings = []
        self.offset = 0

    def ping(self, t: int) -> int:
        self.pings += t,
        
        while self.pings[-1] - self.pings[0] > 3000:
            self.pings.pop(0)
            
        return len(self.pings)


stime = time.time()

obj = RecentCounter()
print(1 == obj.ping(1))
print(2 == obj.ping(100))
print(3 == obj.ping(3001))
print(3 == obj.ping(3002))

print('elapse time: {} sec'.format(time.time() - stime))