import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def encode(self, strs: 'List[str]'):
        if 0 == len(strs):
            return []
        return '#'.join(strs)

    def decode(self, s: str) -> 'List[str]':
        if 0 == len(s):
            return []
        return s.split('#')



stime = time.time()
print(['a', 'b', 'c'] == Solution().decode(Solution().encode(['a', 'b', 'c'])))
print('elapse time: {} sec'.format(time.time() - stime))