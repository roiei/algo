
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List




class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        res = word
        if -1 != idx:
            res = word[idx::-1] + word[idx + 1:]

        return res


stime = time.time()
print("dcbaefd" == Solution().reversePrefix(word = "abcdefd", ch = "d"))
print('elapse time: {} sec'.format(time.time() - stime))