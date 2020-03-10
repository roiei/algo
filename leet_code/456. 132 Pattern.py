import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq



class Solution:
    def find132pattern_ref(self, nums: [int]) -> bool:
        last, stk = float("-inf"), []
        for num in nums[::-1]:

            # num is 1
            # value in the stack is 2
            # last is 3

            # -> it is going to be 132 pattern

            if num < last:
                print('last = ', last)
                break
            while stk and stk[-1] < num:
                last = stk.pop()
            stk += num,
            print('stk = ', stk)
        print(stk[::-1])
        return True if num < last else False


    def find132pattern(self, nums: [int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        last, stk = float("-inf"), []
        for num in nums[::-1]:
            pops = []
            while stk and stk[-1] < num:
                pops += stk.pop(),
            if pops:
                stk += max(pops),
            stk += num,
            print('stk = ', stk)

            if len(stk) == 3 and stk[1] > stk[0] > stk[2]:
                break
        print(stk[::-1])
        if len(stk) < 3:
            return False
        return True if stk[1] > stk[0] > stk[2] else False


stime = time.time()
# print(False == Solution().find132pattern([1, 2, 3, 4]))
# print(True == Solution().find132pattern([3, 1, 4, 2]))
# print(True == Solution().find132pattern([-1, 3, 2, 0]))
print(True == Solution().find132pattern_ref([3,5,0,3,4]))
# print(True == Solution().find132pattern([1,-4,2,-1,3,-3,-4,0,-3,-1]))
print(True == Solution().find132pattern_ref([-2,1,2,-2,1,2]))
print('elapse time: {} sec'.format(time.time() - stime))
