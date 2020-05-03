
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    # timeout
    def findDiagonalOrder(self, nums: [[int]]) -> [int]:
        rows = len(nums)
        bases = []
        cols = []
        mx_cols = 0
        
        for y in range(rows):
            bases += (y, 0),
            cols += len(nums[y]),
            mx_cols = max(mx_cols, len(nums[y]))

        for x in range(1, mx_cols):
            bases += (rows - 1, x),
        
        res = []
        
        while bases:
            y, x = bases.pop(0)

            while y >= 0:
                if x < cols[y]:
                    res += nums[y][x],
                y -= 1
                x += 1
            
        return res


    def findDiagonalOrder(self, nums: [[int]]) -> [int]:
        rows = len(nums)
        cols = []
        mx_cols = 0
        res = []

        for y in range(rows):
            cols += len(nums[y]),
        
        for y in range(rows):
            x = 0
            mx_cols = max(mx_cols, len(nums[y]))

            while y >= 0:
                if x < cols[y]:
                    res += nums[y][x],
                y -= 1
                x += 1

        for x in range(1, mx_cols):
            y = rows - 1

            while y >= 0:
                if x < cols[y]:
                    res += nums[y][x],
                y -= 1
                x += 1

        return res


    def findDiagonalOrder(self, nums):
        rows = len(nums)
        cols = 0

        for y in range(rows):
            cols = max(cols, len(nums[y]))

        diags = []
        for i in range(rows + cols):
            diags += [],

        for y in range(rows):
            for x in range(len(nums[y])):
                diags[y + x].insert(0, nums[y][x])

        res = []
        for diag in diags:
            res += diag

        return res



stime = time.time()
print([1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16] == Solution().findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
print('elapse time: {} sec'.format(time.time() - stime))