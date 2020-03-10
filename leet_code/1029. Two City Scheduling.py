import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def twoCitySchedCost(self, costs: [[int]]) -> int:
        if not costs:
            return 0
    
        mcost = float('inf')
        
        def dfs(costs, n, hn, cost, depth):
            nonlocal mcost
            if n == depth:
                #print(cost)
                mcost = min(mcost, cost)
                return
            if depth < hn:
                dfs(costs, n, hn, cost+costs[depth][0], depth+1)
                dfs(costs, n, hn, cost+costs[depth][1], depth+1)
            else:
                dfs(costs, n, hn, cost+costs[depth][1], depth+1)
                dfs(costs, n, hn, cost+costs[depth][0], depth+1)
        
        dfs(costs, len(costs), len(costs)//2, 0, 0)
        print(mcost)
        return mcost

    def twoCitySchedCost_ref(self, costs: [[int]]) -> int:
        print(costs)
        costs.sort(key=lambda x:x[0]-x[1])
        N = len(costs)//2
        total=0

        print(costs)

        for i in range(len(costs)):
            if i < N:
                total+=costs[i][0]
            else:
                total+=costs[i][1]
        return total
            


stime = time.time()
#print(110 == Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
print(1859 == Solution().twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))
print('elapse time: {} sec'.format(time.time() - stime))

     