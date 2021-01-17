import time
from util.util_list import *
from typing import List


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(map(int, list(str(n))))
            

stime = time.time()
print(8 == Solution().minPartitions("82734"))
print('elapse time: {} sec'.format(time.time() - stime))
