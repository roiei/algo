import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        concat = ''
        for word in words:
            concat += word
            if s == concat:
                return True
        
        return False


stime = time.time()
print(False == Solution().isPrefixString(s = "iloveleetcode", words = ["apples","i","love","leetcode"]))
print('elapse time: {} sec'.format(time.time() - stime))