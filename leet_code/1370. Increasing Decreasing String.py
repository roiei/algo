
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def sortString(self, s: str) -> str:

        ss = collections.Counter(s)
        ss = list(map(list, sorted(ss.items(), key=lambda p: p[0])))
        res = []

        while ss:
            delidx = []
            for i, ch in enumerate(ss):
                res += ss[i][0],
                ss[i][1] -= 1
                if ss[i][1] == 0:
                    delidx += i,

            for i in sorted(delidx, reverse=True):
                del ss[i]

            delidx = []
            for i in range(len(ss) - 1, -1, -1):
                res += ss[i][0],
                ss[i][1] -= 1
                if ss[i][1] == 0:
                    delidx += i,

            for i in sorted(delidx, reverse=True):
                del ss[i]

        return ''.join(res)

            
            
stime = time.time()
# print("abccbaabccba" == Solution().sortString("aaaabbbbcccc"))
# print("art" == Solution().sortString("rat"))
# print("cdelotee" == Solution().sortString("leetcode"))
# print("ops" == Solution().sortString("spo"))
print("ceilmnoprtwoieeoe" == Solution().sortString("eleetminicoworoep"))
print('elapse time: {} sec'.format(time.time() - stime))