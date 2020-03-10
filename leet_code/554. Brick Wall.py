import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall:
            return 0
        holes = collections.defaultdict(int)
        for layer in wall:
            pos = 0
            for i in range(len(layer)-1):
                pos += layer[i]
                holes[pos] += 1
        n = len(wall)        
        thicks = [n - val for val in holes.values()]
        return min(thicks) if thicks else n
            

stime = time.time()
print(2 == Solution().leastBricks([[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]))
print('elapse time: {} sec'.format(time.time() - stime))