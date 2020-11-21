
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect



class Solution:
    def jobScheduling(self, startTime: [int], endTime: [int], profit: [int]) -> int:
        g = collections.defaultdict(dict)
        n = len(startTime)

        for i in range(n):
            for j in range(i, -1, -1):
                if endTime[j] <= startTime[i]:
                    g[j][i] = True
                    break
        
        visited = set()
        mx = 0

        for i in range(n):
            q = [(i, profit[i])]
            visited.add(i)

            while q:
                node, acc = q.pop(0)
                mx = max(mx, acc)
                for adj, linked in g[node].items():
                    if adj in visited:
                        continue

                    visited.add(adj)
                    q += (adj, acc + profit[adj]),

        return mx


    def jobScheduling(self, startTime: [int], endTime: [int], profit: [int]) -> int:
        def latestNonConflict(i):
            for j in range(i - 1, -1, -1):
                if endTime[j] <= startTime[i]:
                    return j
            return -1

        n = len(startTime)
        tbl = [0]*n
        tbl[0] = profit[0]

        for i in range(1, n):
            inc = profit[i]
            l = latestNonConflict(i)
            if l != -1:
                inc += tbl[l]

            tbl[i] = max(inc, tbl[i - 1])

        print(tbl)
        return tbl[-1]


    def jobScheduling(self, startTime: [int], endTime: [int], profit: [int]) -> int:
        class Job:
            def __init__(self, start, finish, profit):
                self.start = start
                self.finish = finish
                self.profit = profit


        def latestNonConflict(i):
            for j in range(i - 1, -1, -1):
                if arr[j].finish <= arr[i].start:
                    return j
            return -1


        n = len(startTime)
        arr = []
        for i in range(n):
            arr += Job(startTime[i], endTime[i], profit[i]),

        arr = sorted(arr, key=lambda p: p.finish < p.start)

        
        tbl = [0]*n
        tbl[0] = arr[0].profit
        mx = 0

        for i in range(1, n):
            inc = arr[i].profit
            l = latestNonConflict(i)
            if l != -1:
                inc += tbl[l]

            tbl[i] = inc
            mx = max(mx, tbl[i])

        print(tbl)
        return mx


    def jobScheduling(self, startTime: [int], endTime: [int], profit: [int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda p: p[1])
        dp = [[0, 0]]

        for s, e, p in jobs:
            i = bisect.bisect_left(dp, [s + 1]) - 1
            
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]














stime = time.time()
print(120 == Solution().jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))
print(150 == Solution().jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]))
print(6 == Solution().jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]))
print('elapse time: {} sec'.format(time.time() - stime))