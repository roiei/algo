import time
from util_list import *


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{:b}'.format(int(a, 2) + int(b, 2))


stime = time.time()
print('100' == Solution().addBinary('11', '1'))
print('elapse time: {} sec'.format(time.time() - stime))
