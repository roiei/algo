import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution:
    def nthSuperUglyNumber_es(self, n: int, primes: [int]) -> int:
        if not primes:
            return 0
        nums = [1]
        cur = 2
        i = 1
        while i < n:
            num = cur
            while num > 1:
                pnum = num
                for p in primes:
                    if 0 == num%p:
                        num //= p
                if pnum == num:
                    break                    
            if 1 == num:
                nums += cur,
                i += 1
            cur += 1
        return nums

    def search(self, nums, num, l, r):
        while l <= r:
            m = (l+r)//2
            if nums[m] == num:
                return m, True
            if nums[m] < num:
                l = m+1
            elif nums[m] > num:
                r = m-1
        return l, False

    def nthSuperUglyNumber_wrong(self, n: int, primes: [int]) -> int:
        if not primes:
            return 0
        nums = [1]
        cur = 2
        i = 1

        def search(nums, num, l, r):
            while l <= r:
                m = (l+r)//2
                if nums[m] == num:
                    return m, True
                if nums[m] < num:
                    l = m+1
                elif nums[m] > num:
                    r = m-1
            return l, False

        step = min(primes)
        limit = step*n
        for i in range(len(primes)):
            for step in range(len(primes)):
                cur = primes[i]
                for j in range(n):
                    print('cur = ', cur, 'step = ', primes[step])
                    idx, found = search(nums, cur, 0, len(nums)-1)
                    if True != found:
                        nums.insert(idx, cur)
                    cur *= primes[step]
                    print('cur = ', cur)
                    print('nums = ', nums)
                    print()
        return nums[n-1]

    def nthSuperUglyNumber_ref(self, n, primes):
        h, heap = set([1]), [1]
        while n:
            a = heapq.heappop(heap)
            for i in primes:
                m = a * i
                if not m in h:
                    heapq.heappush(heap, m)
                    h.add(m)
            n -= 1
        return a

    def nthSuperUglyNumber_ref(self, n, primes):
        done = set()
        nums = [1]
        i = 0
        while i < n:
            cur = heapq.heappop(nums)
            for p in primes:
                val = cur*p
                if val in done:
                    continue
                done.add(val)
                heapq.heappush(nums, val)
            i += 1
        return cur

    def nthSuperUglyNumber_mine(self, n, primes):
        done = set()
        nums = [1]
        i = 0
        while i < n:
            cur = nums[i]
            for p in primes:
                val = cur*p
                if val in done:
                    continue
                done.add(val)
                l, r = 0, len(nums)-1
                idx, found = self.search(nums, val, l, r)
                if False == found:
                    nums.insert(idx, val)
            i += 1
        return nums[n-1]

[1, 3, 5, 7, 9, 11, 15, 19, 21, 23, 27, 29, 33, 41, 43, 45, 47,]
[1, 3, 5, 7, 9, 11, 15, 19, 21, 23, 25, 27, 29, 33, 35]

#print(Solution().nthSuperUglyNumber(15, [3,5,7,11,19,23,29,41,43,47]))
#print(Solution().nthSuperUglyNumber_es(15, [3,5,7,11,19,23,29,41,43,47]))
#print(Solution().nthSuperUglyNumber(12, [2,7,13,19]))
#print(Solution().nthSuperUglyNumber_es(12, [2,7,13,19]))


stime = time.time()
#print(Solution().nthSuperUglyNumber_ref(100000, [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]))
print('elapse time: {} sec'.format(time.time() - stime))
stime = time.time()
print(Solution().nthSuperUglyNumber_mine(12, [2,7,13,19]))

#print(Solution().nthSuperUglyNumber_mine(100000, [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]))


print('elapse time: {} sec'.format(time.time() - stime))


