
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class TweetCounts:

    def __init__(self):
        self.time = collections.defaultdict(list)
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        idx = bisect.bisect_left(self.time[tweetName], time)
        self.time[tweetName].insert(idx, time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        unit = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        
        cur = startTime
        endTime += 1
        res = []
        
        while cur < endTime:
            end_idx = bisect.bisect_left(self.time[tweetName], min(cur + unit, endTime))
            str_idx = bisect.bisect_left(self.time[tweetName], cur)
            
            res += end_idx - str_idx,
            cur += unit
        
        return res
            

            
stime = time.time()
#print(5 == Solution().minSteps(s = "leetcode", t = "practice"))
print('elapse time: {} sec'.format(time.time() - stime))