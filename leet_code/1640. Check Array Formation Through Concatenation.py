
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from functools import lru_cache
import bisect


"""
arr = [91,4,64,78,4], pieces = [[78],[4,64],[91], [4]]

78: [78]
4: [4, 64], [4]
91: [91]

create a dict: O(1)*m
finding: 
    best : n*O(1)
    if dup -> no problem

[1, 1, 3], [[1], [1, 1], 3]


"""


class Solution:
    def canFormArray(self, arr: [int], pieces: [[int]]) -> bool:
        vals = collections.defaultdict(list)
        for piece in pieces:
            vals[piece[0]] += piece,

        def dfs(arr, idx):
            if idx == len(arr):
                return True

            if idx > len(arr):
                return False

            for subseq in vals[arr[idx]]:
                i = 0
                j = idx
                while i < len(subseq):
                    if subseq[i] == arr[j]:
                        i += 1
                        j += 1
                    else:
                        i += 1

                if j - idx == len(subseq):
                    if dfs(arr, j):
                        return True

            return False

        return dfs(arr, 0)

    def canFormArray(self, arr: [int], pieces: [[int]]) -> bool:
        vals = collections.defaultdict(list)
        for piece in pieces:
            vals[piece[0]] += piece,

        idx = 0
        while idx < len(arr):
            pidx = idx
            for subseq in vals[arr[idx]]:
                i = 0
                j = idx
                while i < len(subseq):
                    if subseq[i] == arr[j]:
                        j += 1
                    i += 1

                if j - idx == len(subseq):
                    idx = j
                    break

            if idx == pidx:
                return False

        return True


stime = time.time()
print(True == Solution().canFormArray(arr = [91,4,64,78], pieces = [[78],[4,64],[91]]))
print(True == Solution().canFormArray(arr = [85], pieces = [[85]]))
print('elapse time: {} sec'.format(time.time() - stime))
