import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        min_i = 0
        max_i = len(tokens)-1
        ptr = 0
        mptr = 0
        
        while min_i <= max_i:
            if tokens[min_i] <= P:
                P -= tokens[min_i]
                min_i += 1
                ptr += 1
                mptr = max(mptr, ptr)
            elif ptr > 0:
                ptr -= 1
                P += tokens[max_i]
                max_i -= 1
            elif ptr == 0:
                break
        return mptr



stime = time.time()
print(Solution().bagOfTokensScore([100,200,300,400], 200))
print('elapse time: {} sec'.format(time.time() - stime))