import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution:
    def isStrobogrammatic(self, num):
        mapping = {
            0: 0,
            1: 1,
            6: 9,
            9: 6,
            8: 8
        }
        
        n = len(num)
        num = list(map(int, num))
        
        single_mirrable = [0, 1, 8]
        if n == 1 and num[0] not in single_mirrable:
            return False
            
        n_mirrable = [0, 1, 6, 8, 9]
        for val in num:
            if val not in n_mirrable:
                return False

        for i in range(n//2):
            if not (num[i] == mapping[num[n - 1 - i]] and \
                mapping[num[i]] == num[n - 1 - i]):
                return False

        return True


stime = time.time()
print(True == Solution().isStrobogrammatic("69"))
print(False == Solution().isStrobogrammatic("68"))
#print(False == Solution().isStrobogrammatic(14))
print('elapse time: {} sec'.format(time.time() - stime))
