import time
import re
import collections
from typing import List


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = collections.defaultdict(int)

        for ball in range(lowLimit, highLimit + 1):
            idx = sum(map(int, list(str(ball))))
            boxes[idx] += 1

        boxes = sorted(boxes.items(), key=lambda p: p[1], reverse=True)
        return boxes[0][1]



stime = time.time()
print(2 == Solution().countBalls(lowLimit = 1, highLimit = 10))
print('elapse time: {} sec'.format(time.time() - stime))