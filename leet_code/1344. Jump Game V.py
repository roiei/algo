
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def maxJumps(self, arr: [int], d: int) -> int:
        n = len(arr)

        def jump(idx):
            q = [(idx, 1)]
            visited = set()
            
            mx = 0
            print('>>> idx = ', idx)

            while q:
                idx, cnt = q.pop(0)
                visited.add(idx)
                print(idx, cnt)
                mx = max(cnt, mx)

                for i in range(idx, idx + d + 1):
                    for direction in [-1, 1]:
                        offset = i*direction

                        if not (0 <= offset < n):
                            continue

                        if offset in visited:
                            continue

                        if arr[idx] > arr[offset]:
                            q += (offset, cnt + 1),

            print(mx)
            return mx

        mx = 0
        for i in range(n):
            mx = max(mx, jump(i))

        print(mx)
        return mx


    def maxJumps(self, arr: [int], d: int) -> int:
        n = len(arr)

        def jump(idx):
            
            mx = 0

            for i in range(idx, idx + d + 1):
                for direction in [-1, 1]:
                    offset = i*direction

                    if not (0 <= offset < n):
                        continue

                    if arr[idx] > arr[offset]:
                        mx = max(mx, 1 + jump(offset))

            print(mx)
            return mx

        mx = 0
        for i in range(n):
            mx = max(mx, 1 + jump(i))

        print(mx)
        return mx


    def maxJumps(self, arr: [int], d: int) -> int:
        mem = {}
        n = len(arr)
        
        def jump(idx):
            if idx in mem:
                return mem[idx]
            
            mem[idx] = 1
            
            l = idx - 1
            r = idx + 1
            
            lbound = max(0, idx - d)
            rbound = min(n, idx + d + 1)
            
            while l >= lbound and arr[idx] > arr[l]:
                mem[idx] = max(mem[idx], 1 + jump(l))
                l -= 1
            
            while r < rbound and arr[idx] > arr[r]:
                mem[idx] = max(mem[idx], 1 + jump(r))
                r += 1
          
            return mem[idx]
        
        return max(jump(i) for i in range(n))

            
stime = time.time()
print(4 == Solution().maxJumps(arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2))
print('elapse time: {} sec'.format(time.time() - stime))