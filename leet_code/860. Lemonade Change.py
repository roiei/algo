import time
from util.util_list import *
from util.util_tree import *
import bisect
import copy
import collections
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills:
            return False
        changes = [0]*2
        cost = {}
        cost[0] = 10
        cost[1] = 5
        
        for bill in bills:
            left = bill - 5
            if bill == 5:
                changes[1] += 1
            elif bill == 10:
                changes[0] += 1
            
            if 0 == left:
                continue
            
            for i in range(len(changes)):
                while cost[i] <= left and changes[i] > 0:
                    left -= cost[i]
                    changes[i] -= 1
            if left > 0:
                return False
        return True

    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills:
            return False
        changes = {5:0, 10:0}
        
        for bill in bills:
            if bill == 5:
                changes[5] += 1
            elif bill == 10:
                changes[10] += 1
                if changes[5] < 1:
                    return False                    
                changes[5] -= 1
            elif bill == 20:
                if changes[10] < 1:
                    if changes[5] < 3:
                        return False
                    changes[5] -= 3
                elif changes[10] > 0:
                    changes[10] -= 1
                    if changes[5] < 1:
                        return False
                    changes[5] -= 1
                
        return True

    def lemonadeChange(self, bills: List[int]) -> bool:
        q = []

        for bill in bills:
            paid = bill

            while paid > 5:
                if not q:
                    return False

                pre = paid
                i = len(q) - 1
                while paid > 5 and i >= 0:
                    if paid > q[i]:
                        paid -= q.pop(i)
                    i -= 1
                if pre == paid:
                    return False

            idx = bisect.bisect_left(q, bill)
            q.insert(idx, bill)

        return True


stime = time.time()
# print(True == Solution().lemonadeChange([5,5,5,10,20]))
# print(True == Solution().lemonadeChange([5,5,10]))
# print(False == Solution().lemonadeChange([10,10]))
# print(False == Solution().lemonadeChange([5,5,10,10,20]))
print(False == Solution().lemonadeChange([5,5,5,10,5,5,10,20,20,20]))
print('elapse time: {} sec'.format(time.time() - stime))