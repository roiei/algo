
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def maxPerformance(self, n: int, speed: [int], efficiency: [int], k: int) -> int:

        mx = 0

        def dfs(depth, start, sel_spd, sel_eff):
            nonlocal mx

            if depth == k:
                mx = max(mx, sum(sel_spd)*min(sel_eff))
                return mx

            if sel_spd:
                mx = max(mx, sum(sel_spd)*min(sel_eff))

            for i in range(start, n):
                dfs(depth + 1, i + 1, sel_spd + [speed[i]], sel_eff + [efficiency[i]])

            return mx

        dfs(0, 0, [], [])
        return mx


    def maxPerformance(self, n: int, speed: [int], efficiency: [int], k: int) -> int:
        pq = []
        inc_spd = 0
        mx = 0

        ins = sorted(zip(efficiency, speed), reverse=True)

        while ins:
            eff, spd = ins.pop(0)
            heapq.heappush(pq, spd)
            inc_spd += spd

            if len(pq) > k:
                inc_spd -= heapq.heappop(pq)

            #print('inc_spd = {}, eff = {}, inc_spd*eff = {}'.format(inc_spd, eff, inc_spd*eff))
            mx = max(mx, inc_spd*eff)

        return mx%(10**9 + 7)




        

stime = time.time()
print(60 == Solution().maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2))
# print(56 == Solution().maxPerformance(3, [2,8,2], [2,7,1], 2))
#print(68 == Solution().maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3))
print('elapse time: {} sec'.format(time.time() - stime))