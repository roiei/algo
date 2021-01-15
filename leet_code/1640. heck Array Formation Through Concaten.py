
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from Typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for piece in pieces:
            for item in piece:
                if item in arr:
                    arr.pop(arr.index(item))

        return not arr
                    

stime = time.time()
print(False == Solution().canFormArray([49,18,16], [[16,18,49]]))
print('elapse time: {} sec'.format(time.time() - stime))