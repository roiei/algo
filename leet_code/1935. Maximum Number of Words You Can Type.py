
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        cnt = 0
        for word in text.split():
            if set(word) & set(brokenLetters):
                continue
            
            cnt += 1
        
        return cnt


stime = time.time()
print(1 == Solution().canBeTypedWords(text = "hello world", brokenLetters = "ad"))
print('elapse time: {} sec'.format(time.time() - stime))