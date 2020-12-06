import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect


class Solution:
    def largestNumber(self, nums: [int]) -> str:
        n = len(nums)
        mx = 0

        def dfs(sel, num_sel, seq):
            nonlocal mx

            if num_sel == n:
                mx = max(mx, int(''.join(seq)))
                return

            for i in range(n):
                if i in sel:
                    continue

                sel += i,
                dfs(sel, num_sel + 1, seq + [str(nums[i])])
                sel.pop()

        mem = {}
        dfs([], 0, [])
        return str(mx)

    def largestNumber(self, nums: [int]) -> str:
        if not any(nums):
            return "0"
        
        # def cmp(a, b):
        #     return (a > b) - (a < b)

        def cmp(a, b):
            if a > b:
                return 1
            elif a < b:
                return -1
            return 0
        
        def compare(x, y):
            return cmp(y + x, x + y)
            
        nums = [str(i) for i in nums]
        nums.sort(key=functools.cmp_to_key(compare))
        return "".join(nums)

    def largestNumber(self, nums: [int]) -> str:
        if not any(nums):
            return "0"
        
        def compare(x, y):
            a = y + x
            b = x + y

            if a > b:
                return 1
            elif a < b:
                return -1
            return 0

        def search(val, nums):
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = (l + r)//2
                res = compare(val, nums[m])
                if res == 0:
                    return m
                if res > 0:
                    l = m + 1
                else:
                    r = m - 1

            return l

        nums = [str(i) for i in nums]
        res = []
        for num in nums:
            idx = search(num, res)
            res.insert(idx, num)

        return ''.join(res)

    def largestNumber(self, nums: [int]) -> str:
        if not any(nums):
            return "0"
        
        def compare(x, y):
            a = x + y
            b = y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            return 0

        def search(val, nums):
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = (l + r)//2
                ret = compare(val, nums[m])
                if ret == 0:
                    return m
                if ret > 0:
                    l = m + 1
                else:
                    r = m - 1

            return l

        nums = [str(i) for i in nums]
        res = []
        for num in nums:
            idx = search(num, res)
            res.insert(idx, num)

        return ''.join(res[::-1])


# a = 8247
# b = 824
#
# 8247 824
# 824 8247   <- the bigger (b + a)



"9609 938 8247 824  69735703560743981399"
"9609 938 824 8247  69735703560743981399"

# 비교 시 더 짧은 경우 나의 마지막에 나와 같은 값을 적용 한 것과 더 긴 것의 가장 맨 앞 자리를 비교

stime = time.time()
print("9609938824824769735703560743981399" == Solution().largestNumber([824,938,1399,5607,6973,5703,9609,4398,8247]))
print("9534330" == Solution().largestNumber([3,30,34,5,9]))
#print("0" == Solution().largestNumber([0,0]))
#print("0" == Solution().largestNumber([0,0]))
#print("210" == Solution().largestNumber([10,2]))
#print("34330" == Solution().largestNumber([30,34,3]))
print('elapse time: {} sec'.format(time.time() - stime))

