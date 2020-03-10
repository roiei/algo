
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def subarraysWithKDistinct(self, A: [int], K: int) -> int:
        freq = collections.defaultdict(int)
        
        cnt = i = j = 0
        kind = 0
        
        n = len(A)
        
        while i < n and j < n:
            if freq[A[i]] == 0:
                kind += 1
            freq[A[i]] += 1

            while kind > K and j < n:
                freq[A[j]] -= 1
                if freq[A[j]] == 0:
                    kind -= 1
                    
                j += 1

            #print('freq = {}, i = {}, j = {}'.format(freq, i, j))
            
            if kind == K:
                cnt += i - j - (K - 2)

            i += 1
        
        return cnt

    def subarraysWithKDistinct2(self, A: [int], K: int) -> int:
        
        def add(freq, val):
            offset = 0
            if freq[val] == 0:
                offset += 1
            freq[val] += 1
            return offset
        
        def remove(freq, val):
            offset = 0
            freq[val] -= 1
            if freq[val] == 0:
                offset = 1
            return offset
            
        freq1 = collections.defaultdict(int)
        kind1 = 0
        freq2 = collections.defaultdict(int)
        kind2 = 0
        
        j = i = 0
        cnt = 0

        for right, num in enumerate(A):
            kind1 += add(freq1, num)
            kind2 += add(freq2, num)

            while kind1 > K:
                kind1 -= remove(freq1, A[j])
                j += 1

            while kind2 >= K:
                kind2 -= remove(freq2, A[i])
                i += 1

            cnt += i - j

        return cnt
            


stime = time.time()

#print(7 == Solution().subarraysWithKDistinct(A = [1,2,1,2,3], K = 2))
#print(3 == Solution().subarraysWithKDistinct(A = [1,2,1,3,4], K = 3))
print(23 == Solution().subarraysWithKDistinct([2,2,1,2,2,2,1,1], 2))
print('elapse time: {} sec'.format(time.time() - stime))