import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: [int], N: int) -> [int]:
        for i in range(N):
            nex = [0]*len(cells)
            for j in range(1, len(cells) - 1):
                if j == 0 or j == len(cells) - 1:
                    nex[j] = 0
                    continue

                if ((cells[j - 1] == 0 and cells[j + 1] == 0) or 
                    (cells[j - 1] == 1 and cells[j + 1] == 1)):
                    nex[j] = 1
                else:
                    nex[j] = 0

            cells = nex

        return cells

    def prisonAfterNDays(self, cells, N):
        seen = {tuple(cells): N}

        while N:
            if tuple(cells) not in seen:
                seen[tuple(cells)] = N

            N -= 1

            nex = [0]*len(cells)
            for i in range(1, len(cells) - 1):
                nex[i] = cells[i - 1] ^ cells[i + 1] ^ 1
            cells = nex

            if tuple(cells) in seen:
                N %= seen[tuple(cells)] - N
        return cells


stime = time.time()
print([0,0,1,1,0,0,0,0] == Solution().prisonAfterNDays(cells = [0,1,0,1,1,0,0,1], N = 7))
print('elapse time: {} sec'.format(time.time() - stime))

