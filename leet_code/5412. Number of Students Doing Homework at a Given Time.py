
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def busyStudent(self, startTime: [int], endTime: [int], queryTime: int) -> int:
        cnt = 0
        for s, e in list(zip(startTime, endTime)):
            if s <= queryTime <= e:
                cnt += 1
        return cnt


stime = time.time()
print(1 == Solution().busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4))
print('elapse time: {} sec'.format(time.time() - stime))