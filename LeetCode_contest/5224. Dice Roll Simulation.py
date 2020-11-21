
import time
import copy
import collections


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
        

stime = time.time()
print(34 == Solution().dieSimulator(n = 2, rollMax = [1,1,2,2,2,3]))
print(30 == Solution().dieSimulator(n = 2, rollMax = [1,1,1,1,1,1]))
print(181 == Solution().dieSimulator(n = 3, rollMax = [1,1,1,2,2,3]))
print('elapse time: {} sec'.format(time.time() - stime))