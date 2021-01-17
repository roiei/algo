import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        mx = 0
        tot = 0
        idxs = collections.defaultdict(int)
        
        for r, num in enumerate(nums):
            if num in idxs and idxs[num] >= l:
                idx = idxs[num]
                
                for idx in range(l, idx + 1):
                    tot -= nums[idx]
                
                l = idx + 1
                
            idxs[num] = r
            tot += num            
            mx = max(mx, tot)
        
        return mx
                

stime = time.time()
sol = Solution()
print(8 == sol.maximumUniqueSubarray(nums = [5,2,1,2,5,2,1,2,5]))
print(30934 == sol.maximumUniqueSubarray([449,154,934,526,429,732,784,909,884,805,635,660,742,209,742,272,669,449,766,904,698,434,280,332,876,200,333,464,12,437,269,355,622,903,262,691,768,894,929,628,867,844,208,384,644,511,908,792,56,872,275,598,633,502,894,999,788,394,309,950,159,178,403,110,670,234,119,953,267,634,330,410,137,805,317,470,563,900,545,308,531,428,526,593,638,651,320,874,810,666,180,521,452,131,201,915,502,765,17,577,821,731,925,953,111,305,705,162,994,425,17,140,700,475,772,385,922,159,840,367,276,635,696,70,744,804,63,448,435,242,507,764,373,314,140,825,34,383,151,602,745]))
print('elapse time: {} sec'.format(time.time() - stime))
