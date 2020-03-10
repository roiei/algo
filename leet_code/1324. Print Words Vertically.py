
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def printVertically(self, s: str) -> [str]:
        s = s.split()
        mx = max(s, key=len)
        n = len(mx)
        res = []

        for i in range(len(s)):
            s[i] = s[i] + (n - len(s[i]))*' '

        for i in range(n):
            line = ''
            for word in s:
                line += word[i]

            res += line.rstrip(),

        return res

       

stime = time.time()
#print(["HAY","ORO","WEU"] == Solution().printVertically(s = "HOW ARE YOU"))
print(["CIC","OSO","N M","T I","E N","S G","T"] == Solution().printVertically("CONTEST IS COMING"))
print('elapse time: {} sec'.format(time.time() - stime))