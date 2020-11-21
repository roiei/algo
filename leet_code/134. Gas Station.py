import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        tot = sum(diff)
        if tot < 0:
            return -1
        
        n = len(gas)
        i = 0
        
        while i < n:
            if diff[i] >= 0:
                seq = diff[i:] + diff[:i]
                tot = 0
                for j in range(len(seq)):
                    tot += seq[j]
                    if tot < 0:
                        break
                else:
                    return i
            i += 1
        
        return -1

    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        mn_idx = None
        tot = 0
        mn = float('inf')
        n = len(gas)

        for i, diff in enumerate([g - c for g, c in list(zip(gas, cost))]):
            tot += diff

            if tot < mn:
                mn = tot
                mn_idx = (i + 1)%n
                
        return -1 if tot < 0 else mn_idx

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        for i in range(n):
            gas_cost = list(zip(gas[i:] + gas[:i], cost[i:] + cost[:i]))
            inc = 0
            for g, c in gas_cost:
                inc += g
                inc -= c
                
                if inc < 0:
                    break
            else:
                return i
        
        return -1


stime = time.time()
print(3 == Solution().canCompleteCircuit(gas  = [1,2,3,4,5], cost = [3,4,5,1,2]))
print('elapse time: {} sec'.format(time.time() - stime))