
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List



class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for op in operations:
            if '--' in op:
                res -= 1
            elif '++' in op:
                res += 1

        return res


stime = time.time()
print(1 == Solution().finalValueAfterOperations(operations = ["--X","X++","X++"]))
print('elapse time: {} sec'.format(time.time() - stime))