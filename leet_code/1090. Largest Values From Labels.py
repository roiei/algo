
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def largestValsFromLabels(self, values: [int], labels: [int], num_wanted: int, use_limit: int) -> int:
        
        values = list(zip(values, labels))        
        values.sort(key=lambda p: p[0], reverse=True)
        res = collections.defaultdict(list)
        cnt = 0
        
        for v, label in values:
            if cnt >= num_wanted:
                break
                
            if len(res[label]) < use_limit:
                res[label] += v,
                cnt += 1
        
        return sum([sum(l) for l in res.values()])



stime = time.time()
print(12 == Solution().largestValsFromLabels([5,4,3,2,1], [1,3,3,3,2], 3, 2))
print('elapse time: {} sec'.format(time.time() - stime))