
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def maxPoints(self, points):
        if not points:
            return 0

        mx = 0
        for i, coord1 in enumerate(points):
            freq = collections.defaultdict(int)
            same = 0
            x1, y1 = coord1
            
            for x2, y2 in points[:i] + points[i + 1:]:
                if x1 == x2 and y1 == y2:
                    same += 1
                    continue

                if y1 - y2 == 0:
                    k = 0xF00B00A # magic number
                else:
                    k = (x1 - x2)/(y1 - y2)

                freq[k] += 1
                
            mx = max(mx, max(freq.values() if freq.values() else [0]) + same)

        return mx + 1
        
            
stime = time.time()
print(3 == Solution().maxPoints([[1,1],[2,2],[3,3]]))
print(4 == Solution().maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
print('elapse time: {} sec'.format(time.time() - stime))