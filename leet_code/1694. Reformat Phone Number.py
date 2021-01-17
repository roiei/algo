import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = [num for num in number if num.isdigit()]
        size = len(digits)
        res = []
        
        while size:
            if size == 4:
                res += digits[:2] + ['-'] + digits[2:]
                break
            elif size < 4:
                res += digits[:]
                break
            else:
                res += digits[:3] + ['-']
                digits = digits[3:]
                size -= 3
        
        return ''.join(res)


stime = time.time()
sol = Solution()
print("123-456" == sol.reformatNumber("1-23-45 6"))
print("123-45-67" == sol.reformatNumber("123 4-567"))
print('elapse time: {} sec'.format(time.time() - stime))
