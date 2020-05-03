
import time
import copy
import collections


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        def get_steps(num):
            step = 0

            while num != 1:
                if num%2 == 0:
                    num //= 2
                else:
                    num = num*3 + 1
                step += 1

            return step

        steps = collections.defaultdict(int)
        for num in range(lo, hi + 1):
            steps[num] = get_steps(num)

        steps = sorted(steps.items(), key=lambda p: p[1])
        return steps[k - 1][0] if k <= len(steps) else -1



stime = time.time()
print(13 == Solution().getKth(lo = 12, hi = 15, k = 2))
print('elapse time: {} sec'.format(time.time() - stime))