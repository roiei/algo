
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ' '
        freq = [['a', a], ['b', b], ['c', c]]

        def fill_res(idx, n):
            inc = n if freq[idx][1] >= n else freq[idx][1]
            ret = freq[idx][0]*inc
            freq[idx][1] -= inc
            return ret

        while freq:
            freq.sort(key=lambda p: p[1], reverse=True)

            if res[-1] != freq[0][0]:
                ret = fill_res(0, 2)
                if not ret:
                    break

                res += ret
            elif len(freq) > 1:
                ret = fill_res(1, 1)
                if not ret:
                    break

                res += ret
            else:
                break

        return len(res[1:])



stime = time.time()
print("ccaccbcc" == Solution().longestDiverseString(a = 1, b = 1, c = 7))
# print("aabbc" == Solution().longestDiverseString(a = 2, b = 2, c = 1))
# print("aabaa" == Solution().longestDiverseString(a = 7, b = 1, c = 0))
print(len("ccbccbbccbbccbbccbc") == Solution().longestDiverseString(a = 0, b = 8, c = 11))
# print('elapse time: {} sec'.format(time.time() - stime))