
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for val in A:
            res += val**2,
        
        return sorted(res)
                    


stime = time.time()
print('elapse time: {} sec'.format(time.time() - stime))