import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
import functools


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @functools.lru_cache(None)
        def dfs(start, prev, prev_cnt, k): #count the cost of compressing from the start
            if k < 0:
                return float('inf')

            if start >= len(s):
                return 0

            if s[start] == prev:
                incr = 1 if prev_cnt == 1 or prev_cnt == 9 or prev_cnt == 99 else 0
                return incr + dfs(start + 1, prev, prev_cnt + 1, k)
            else:
                keep_counter = 1 + dfs(start + 1, s[start], 1, k)
                del_counter =  dfs(start + 1, prev, prev_cnt, k - 1)
                return min(keep_counter, del_counter)
            
        return dfs(0, "", 0, k)

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        def dfs(start, prev, prev_cnt, k):
            if k < 0:
                return float('inf')

            if start >= len(s):
                return 0

            if s[start] == prev:
                offset = 0
                if prev_cnt == 1 or len(str(prev_cnt)) == str(prev_cnt).count('9'):
                    offset += 1
                return offset + dfs(start + 1, prev, prev_cnt + 1, k)
            else:
                res1 = 1 + dfs(start + 1, s[start], 1, k)
                res2 = dfs(start + 1, prev, prev_cnt, k - 1)
                return min(res1, res2) 

        print(dfs(0, "", 0, k))
        return dfs(0, "", 0, k)


stime = time.time()
#print(4 == Solution().getLengthOfOptimalCompression(s = "aaabcccd", k = 2))
#print(3 == Solution().getLengthOfOptimalCompression("aaaaaaaaaaa", 0))
print(4 == Solution().getLengthOfOptimalCompression("llllllllllttttttttt", 1))
print('elapse time: {} sec'.format(time.time() - stime))