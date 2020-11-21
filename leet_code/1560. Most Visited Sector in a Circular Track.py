import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def mostVisited(self, n: int, rounds: [int]) -> [int]:
        freq = collections.defaultdict(int)
        cur = rounds.pop(0)
        
        while rounds:
            end = rounds.pop(0)
            
            while cur != end:
                freq[cur] += 1

                cur = (cur + 1)%n
            
            freq[end] += 1
            cur = end + 1
        
        freq = sorted(freq.items(), key=lambda p: p[1], reverse=True)
        most = freq[0][1]
        return [k for k, v in freq if v == most]
            

stime = time.time()
print([1,2,3,4,5,6,7] == Solution().mostVisited(n = 7, rounds = [1,3,5,7]))
print([1,2,3,4,5,6,7] == Solution().mostVisited(n = 7, rounds = [1,3,5,7]))
print('elapse time: {} sec'.format(time.time() - stime))