
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def isStrobogrammatic(self, num):
        mapping = collections.defaultdict(list)
        mapping[0] = [0]
        mapping[1] = [1]
        mapping[6] = [6, 9]
        mapping[9] = [9, 6]
        mapping[8] = [8]
        
        n = len(num)
        num = list(map(int, num))
        
        single_mirrable = [0, 1, 8]
        if n == 1 and num[0] not in single_mirrable:
            return False
            
        n_mirrable = [0, 1, 6, 8, 9]
        for val in num:
            if val not in n_mirrable:
                return False
        
        m = n//2
        l, r = m - 1, m + 1
        
        if n%2 == 0:
            l = m - 1
            r = m
        
        while l >= 0 and r < n:
            if not (num[r] in mapping[num[l]] and num[l] in mapping[num[r]]):
                return False
            l -= 1
            r += 1
        
        return True


stime = time.time()
print(True == Solution().isStrobogrammatic("69"))
print(False == Solution().isStrobogrammatic("68"))
print('elapse time: {} sec'.format(time.time() - stime))