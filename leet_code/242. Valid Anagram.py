import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if ''.join(sorted([ch for ch in s])) == ''.join(sorted([ch for ch in t])) else False


stime = time.time()
print(Solution().isAnagram('a', 'b'))
print('elapse time: {} sec'.format(time.time() - stime))