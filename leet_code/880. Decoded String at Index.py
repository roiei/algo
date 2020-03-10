import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        code = {}
        modValues = []
        length = 0
        
        for i in range(0, len(S)):
            if S[i].isdigit():
                modValues.insert(0, length)
                length = length * int(S[i])
            else:
                code[length] = S[i]
                length += 1

        K = K - 1

        for modValue in modValues:
            if K in code:
                return code[K]
            else:
                K = K % modValue

        return code[K]


stime = time.time()
sol = Solution()
print('o' == sol.decodeAtIndex("leet2code3", 10))
print('elapse time: {} sec'.format(time.time() - stime))
