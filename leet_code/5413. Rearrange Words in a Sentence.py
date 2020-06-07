
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def arrangeWords(self, text: str) -> str:
        strs = [(s, len(s)) for s in text.split()]
        strs.sort(key=lambda p: p[1])
        return ' '.join([s for s, l in strs]).capitalize()
        
        

stime = time.time()
print("Is cool leetcode" == Solution().arrangeWords(text = "Leetcode is cool"))
print('elapse time: {} sec'.format(time.time() - stime))