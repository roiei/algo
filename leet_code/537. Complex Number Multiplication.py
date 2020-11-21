
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a, ai = a.split('+')
        b, bi = b.split('+')

        ai = ai[:-1]
        bi = bi[:-1]

        a = int(a)
        b = int(b)
        ai = int(ai)
        bi = int(bi)

        real = a*b - ai*bi    # i^2 == -1
        comp = a*bi + ai*b

        return str(real) + '+' + str(comp) + 'i'
                

stime = time.time()
print("0+2i" == Solution().complexNumberMultiply("1+1i", "1+1i"))
print('elapse time: {} sec'.format(time.time() - stime))

