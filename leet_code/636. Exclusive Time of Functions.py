
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def get_log(self, logs):
        for log in logs:
            data = log.split(':')
            fid, op, ts = int(data[0]), data[1], int(data[2])
            yield fid, op, ts

    def exclusiveTime(self, n: int, logs: [str]) -> [int]:
        stk = []
        elapse = collections.defaultdict(int)
        pre_ts = None
        
        for fid, op, ts in self.get_log(logs):
            if op == 'start':
                if stk:
                    stk[-1] += ts - pre_ts
                stk += 0,
            else:
                elapse[fid] += stk[-1] + ts - pre_ts + 1
                stk.pop()

            pre_ts = ts

            if op == 'end':
                pre_ts += 1
        
        elapse = [v for k, v in sorted(elapse.items(), key=lambda p: p[0])]
        return elapse

    def exclusiveTime(self, n, logs):
        stk, res = [], [0]*n

        for fid, op, ts in self.get_log(logs):
            if op == 'start':
                stk.append((fid, op, ts))
            else:
                accu_time = 0
                while stk[-1][1] != 'start':
                    accu_time += stk.pop()[2]

                start = stk.pop()
                fid, total_time = start[0], ts - start[2] - accu_time + 1
                res[fid] += total_time
                accu_time += total_time
                stk.append((-1, 'accu', accu_time))

        return res


stime = time.time()
print([3, 4] == Solution().exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
#print(Solution().exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6", '2:start:4', '2:end:6']))
#print(Solution().exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6", '2:start:6', '2:end:6']))
print('elapse time: {} sec'.format(time.time() - stime))