
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def leastInterval(self, tasks: [str], n: int) -> int:
        freq = collections.Counter(tasks)
        freq = sorted(freq.values(), reverse=True)
        
        num_intervals = freq[0] - 1
        req_slots = num_intervals*n
        
        for i in range(1, len(freq)):
            req_slots -= min(num_intervals, freq[i])
        
        if req_slots < 0:
            req_slots = 0
        
        return len(tasks) + req_slots

    def leastInterval2(self, tasks: [str], n: int) -> int:
        c = collections.Counter(tasks)
        vals = sorted(c.values(), reverse = True)
        
        max_val = vals[0] - 1
        max_idle_slots = max_val*n
        vals.pop(0)

        for val in vals:
            max_idle_slots -= min(max_val, val)

        return max_idle_slots + len(tasks) if max_idle_slots > 0 else len(tasks)

    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        freq = sorted(freq.items(), key=lambda p: p[1], reverse=True)
        
        mx_num = freq[0][1] - 1
        freq = [(task, num) if num <= mx_num else (task, num - 1) for task, num in freq]
        
        num_pad = mx_num*n
        
        for i in range(1, len(freq)):
            num_pad -= freq[i][1]
        
        if num_pad < 0:
            num_pad = 0
        
        return len(tasks) + num_pad
        

stime = time.time()
print(8 == Solution().leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
#print(Solution().leastInterval(tasks = ["A","A","A","B","B","B"], n = 1))
#print(6 == Solution().leastInterval(tasks = ["A","A","A","B","B","B"], n = 0))
print(104 == Solution().leastInterval(tasks = ["A","A","A","B","B","B"], n = 50))
#print(Solution().leastInterval(tasks = ['A', 'B'], n = 2))
print(10 == Solution().leastInterval(["A","B","C","D","E","A","B","C","D","E"], 4))
print(16 == Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
print('elapse time: {} sec'.format(time.time() - stime))