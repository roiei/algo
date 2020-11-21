
import time
import copy
import collections


class Solution(object):
    def maxEqualFreq(self, nums):
        cnt = collections.defaultdict(int)
        freq = collections.defaultdict(int)
        mx = 0
        res = 0
        
        for i, num in enumerate(nums):
            cnt[num] += 1
            freq[cnt[num] - 1] -= 1
            freq[cnt[num]] += 1
            
            mx = max(mx, cnt[num])
            
            if mx*freq[mx] == i or (mx - 1)*(freq[mx - 1] + 1) == i or mx == 1:
                res = i + 1

        return res
        

stime = time.time()
print(7 == Solution().maxEqualFreq([2,2,1,1,5,3,3,5]))
print(13 == Solution().maxEqualFreq([1,1,1,2,2,2,3,3,3,4,4,4,5]))
print(5 == Solution().maxEqualFreq([1,1,1,2,2,2]))
print(8 == Solution().maxEqualFreq([10,2,8,9,3,8,1,5,2,3,7,6]))
print('elapse time: {} sec'.format(time.time() - stime))