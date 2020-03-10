import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def openLock(self, deadends: [str], target: str) -> int:
        if '0000' in deadends:
            return -1
        deadends = set(deadends)
        q = [('0000', 0)]

        while q:
            nums, depth = q.pop(0)
            for i in range(4):
                for offset in [1, -1]:
                    next_nums = nums[:i] + str((int(nums[i])+offset)%10) + nums[i+1:]
                    if next_nums == target:
                        return depth+1
                    if next_nums not in deadends:
                        q += (next_nums, depth+1),
                        deadends.add(next_nums)

        return -1

    def openLock(self, deadends: [str], target: str) -> int:
        if '0000' in deadends:
            return -1
        mdepth = float('inf')
        deadends = set(deadends)
        q = [('0000', 0)]
        while q:
            nums, depth = q.pop(0)
            if nums == target:
                mdepth = min(mdepth, depth)
                continue
            
            for i in range(4):
                for offset in [1, -1]:
                    nnum = nums[:i] + str((int(nums[i])+offset)%10) + nums[i+1:]
                    if nnum not in deadends:
                        q += (nnum, depth+1), 
                        deadends.add(nnum)

        return mdepth if mdepth != float('inf') else -1


    def openLock(self, deadends: [str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        visited = set(deadends)
        q = [('0000', 0)]

        while q:
            cur, depth = q.pop(0)
            if cur == target:
                return depth
            
            for i in range(4):
                for move in [-1, 1]:
                    ncur = cur[:i] + str((int(cur[i])+move)%10) + cur[i+1:]
                    if ncur not in visited:
                        q += (ncur, depth+1),
                        visited.add(ncur)
        return -1

    def openLock(self, deadends, target):
        if '0000' in deadends:
            return -1
        
        visit = set()
        target = [int(ch) for ch in target]
        start = [int(ch) for ch in '0000']
        visit.add(tuple(start))
        
        for deadend in deadends:
            visit.add(tuple([int(ch) for ch in deadend]))
        
        q = [(start, 0)]
        while q:
            nums, cnt = q.pop(0)
            for i in range(4):
                for offset in [-1, 1]:
                    new_nums = nums[:]
                    new_nums[i] = (new_nums[i] + offset)%10
                    if new_nums == target:
                        return cnt + 1
                    if tuple(new_nums) in visit:
                        continue
                    visit.add(tuple(new_nums))
                    q += (new_nums, cnt + 1),
        return -1


stime = time.time()
#print(Solution().openLock_ref(["0201","0101","0102","1212","2002"], "0202"))
print(Solution().openLock(["0201","0101","0102","1212","2002"], "0202"))
print('elapse time: {} sec'.format(time.time() - stime))


