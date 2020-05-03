
import time
import copy
import collections


class Solution:
    def findTheDistanceValue(self, arr1: [int], arr2: [int], d: int) -> int:
        cnt = 0
        
        for l in arr1:
            for r in arr2:
                if abs(l - r) <= d:
                    break
            else:
                cnt += 1
            
        return cnt


stime = time.time()
print(2 == Solution().longestPrefix(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))
print('elapse time: {} sec'.format(time.time() - stime))