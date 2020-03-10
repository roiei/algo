import time
import random


class Solution:
    def readBinaryWatch(self, num: int) -> 'List[str]':
        n = 10
        bins = ['0']*n

        def dfs(bins, k, start, res):
            if k == 0:
                hour = int(''.join(bins[:4]), 2)
                minute = int(''.join(bins[4:]), 2)
                if hour < 12 and minute < 60:
                    res += '{:01}:{:02}'.format(hour, minute),
            for i in range(start, n):
                bins[i] = '1'
                dfs(bins, k - 1, i + 1, res)
                bins[i] = '0'
            
        res = []
        dfs(bins, num, 0, res)
        return res


stime = time.time()
print(Solution().readBinaryWatch(2)) # ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
print('elapse time: {} sec'.format(time.time() - stime))

