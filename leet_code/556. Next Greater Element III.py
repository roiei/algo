import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        length = len(str(n))
        
        def dfs(seq, sel, depth, res):
            if depth == length:
                res += int(''.join(seq)),
                return
        
            for i in range(length):
                if i in sel:
                    continue
                
                sel += i,
                dfs(seq + [nums[i]], sel, depth + 1, res)
                sel.pop()
        
        nums = list(str(n))
        res = []
        dfs([], [], 0, res)
        mx = max(res)
        res.sort()
        
        for num in res:
            if num > n:
                return num
        
        return -1
                
    def nextGreaterElement(self, n: int) -> int:
        nums = list(map(int, list(str(n))))
        
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        
        for k in range(len(nums) - 1, i - 1, -1):
            if nums[i - 1] < nums[k]:
                break
        
        nums[i - 1], nums[k] = nums[k], nums[i - 1]
        nums[i:] = nums[i:][::-1]
        
        num = int(''.join(map(str, nums)))
        if num > 2**31 or num < -2**31:
            return -1
    
        return num if num > n else -1
        


stime = time.time()
print(213 == Solution().nextGreaterElement(132))
# print(-1 == Solution().nextGreaterElement(
# 21))
# print(13222344 == Solution().nextGreaterElement(
# 12443322))
print(-1 == Solution().nextGreaterElement(
21))
print(-1 == Solution().nextGreaterElement(
1999999999))
print(-1 == Solution().nextGreaterElement(
2147483647))
print('elapse time: {} sec'.format(time.time() - stime))