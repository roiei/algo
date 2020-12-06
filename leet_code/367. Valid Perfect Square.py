import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq



class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = int(num**(1/2))
        return root*root == num


stime = time.time()
print(False == Solution().isPerfectSquare(14))
print('elapse time: {} sec'.format(time.time() - stime))
