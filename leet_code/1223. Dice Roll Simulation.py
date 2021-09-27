import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        num_dice = 6
        tot = num_dice
        
        cont_dies = {}
        sum_dies = {}
        kinds = []
        
        for i in range(num_dice):
            cont_dies[str(i)] = [0 for _ in range(rollMax[i])]
            kinds += str(i),
        
        for kind in kinds:
            cont_dies[kind][0] = 1
            sum_dies[kind] = 1
                    
        for i in range(1, n):
            inc = 0
            
            for kind in kinds:
                pop_num = cont_dies[kind].pop()
                new_num = tot - sum_dies[kind]
                sum_dies[kind] += (new_num - pop_num)
                cont_dies[kind].insert(0, new_num)
                inc += (new_num - pop_num)
                
            tot += inc
            
        return tot % 1000000007

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        cases = collections.defaultdict(int)
        
        for i in range(1, n + 1):
            not_allowed = n - i
            if not_allowed == 0:
                continue
            case = 1
            
            for j in range(1, not_allowed):
                case += 5**j*(j + 1)
                
            cases[i] = case
        
        tot = 6**n

        print(cases)

        for roll in rollMax:
            tot -= cases[roll]
        
        print(tot)
        return tot % (10**9 + 7)
        

stime = time.time()
print(34 == Solution().dieSimulator(n = 2, rollMax = [1,1,2,2,2,3]))
print(30 == Solution().dieSimulator(n = 2, rollMax = [1,1,1,1,1,1]))
print(181 == Solution().dieSimulator(n = 3, rollMax = [1,1,1,2,2,3]))
print(1082 == Solution().dieSimulator(4, [2,1,1,3,3,2]))
print('elapse time: {} sec'.format(time.time() - stime))