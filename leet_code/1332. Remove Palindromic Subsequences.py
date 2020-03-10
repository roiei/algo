
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        s = list(s)
        cnt = 0

        while s:
            if s == s[::-1]:
                cnt += 1
                break
            s = [ch for ch in s if ch != 'a']
            cnt += 1

        return cnt
            

stime = time.time()
# print(1 == Solution().removePalindromeSub("ababa"))
# print(2 == Solution().removePalindromeSub("abb"))
# print(2 == Solution().removePalindromeSub("baabb"))
print(2 == Solution().removePalindromeSub("bbaabaaa"))
# print(0 == Solution().removePalindromeSub(""))
print('elapse time: {} sec'.format(time.time() - stime))