import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def shoppingOffers(self, price, special, needs):
        memo = {}

        def dfs(needs):
            if tuple(needs) in memo:
                return memo[tuple(needs)]

            cost = sum(n*p for n, p in zip(needs, price))
            print(cost)

            for s in special:
                left = []
                for i, n in enumerate(needs):
                    if n < s[i]:
                        break
                    left.append(n-s[i])
                else:
                    cost = min(cost, memo.get(tuple(left), dfs(left)) + s[-1])
            memo[tuple(needs)] = cost
            return cost

        return dfs(needs)

    
    def shoppingOffers(self, price, special, needs):

        def dfs(needs):
            cost = sum(n*p for n, p in zip(needs, price))
            print(cost)

            for s in special:
                left = []
                for i, n in enumerate(needs):
                    if n < s[i]:
                        break
                    left.append(n-s[i])
                else:
                    cost = min(cost, dfs(left) + s[-1])
            return cost

        return dfs(needs)


    def shoppingOffers(self, price, special, needs):
        
        def dfs(needs):
            costs = []
            for sp in special:
                new_needs = []
                for i in range(len(needs)):
                    if needs[i] < sp[i]:
                        break
                    new_needs += needs[i] - sp[i],
                else:
                    costs += dfs(new_needs) + sp[-1],
            costs += sum([p*n for p, n in zip(price, needs)]),
            return min(costs)
        
        return dfs(needs)


    def shoppingOffers(self, price, special, needs):
        n = len(needs)

        def dfs(needs):
            costs = []
            for sp in special:
                new_needs = []
                for i in range(len(needs)):
                    if needs[i] < sp[i]:
                        break
                    new_needs += needs[i] - sp[i],
                else:
                    costs += dfs(new_needs) + sp[-1],
            costs += sum([p*n for p, n in zip(price, needs)]),
            return min(costs)
        
        return dfs(needs)



stime = time.time()
print(14 == Solution().shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]))
#print(11 == Solution().shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]))
print('elapse time: {} sec'.format(time.time() - stime))