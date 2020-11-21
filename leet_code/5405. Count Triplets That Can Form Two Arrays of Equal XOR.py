
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def countTriplets(self, arr: [int]) -> int:
        n = len(arr)
        cnt = 0
      
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    xor1 = 0
                    xor2 = 0
      
                    for idx in range(i, j):
                        xor1 ^= arr[idx]
      
                    for idx in range(j, k + 1):
                        xor2 ^= arr[idx]
      
                    if xor1 == xor2:
                        cnt += 1
        return cnt

    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        total = 0
        res = 0
        hashmap = collections.defaultdict(list)
        hashmap[0] = [-1]
        for i, v in enumerate(arr):
            total ^= v
            print(i, total)
            if total in hashmap:
                for j in hashmap[total]:
                    res += i - j - 1
            hashmap[total].append(i)
        return res

    def countTriplets(self, arr: List[int]) -> int:
        cum = [0]
        for n in arr:
            cum.append(cum[-1]^n)
        ans=0
        for i in range(0, len(arr)-1):
            for k in range(i+1, len(arr)):
                for j in range(i+1, k+1):
                    if cum[i]^cum[j] == cum[k+1]^cum[j]:
                        ans += 1
        return ans


stime = time.time()
print(4 == Solution().countTriplets(arr = [2,3,1,6,7]))
print('elapse time: {} sec'.format(time.time() - stime))