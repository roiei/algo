
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))
        

stime = time.time()
print("1[.]1[.]1[.]1" == Solution().defangIPaddr("1.1.1.1"))
print('elapse time: {} sec'.format(time.time() - stime))