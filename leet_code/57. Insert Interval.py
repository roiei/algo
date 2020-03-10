import time
import random


class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        intervals += newInterval,
        intervals.sort(key=lambda p:p[0], reverse=False)
        
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i][0] = min(intervals[i][0], intervals[i + 1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.pop(i + 1)
            else:
                i += 1
        
        return intervals


stime = time.time()
print([[1,5],[6,9]] == Solution().insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
print([[1,2],[3,10],[12,16]] == Solution().insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
print('elapse time: {} sec'.format(time.time() - stime))

