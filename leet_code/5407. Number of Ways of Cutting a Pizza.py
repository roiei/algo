
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def ways(self, pizza: [str], k: int) -> int:
        

                

stime = time.time()
print(3 == Solution().ways(pizza = ["A..","AAA","..."], k = 3))
# print(1 == Solution().ways(pizza = ["A..","AA.","..."], k = 3))
# print(1 == Solution().ways(pizza = ["A..","A..","..."], k = 1))
print('elapse time: {} sec'.format(time.time() - stime))