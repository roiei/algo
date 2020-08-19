import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        n = len(matrix[0])

        def search(nums, l, r, target):
            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    return m, True
                if nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            return l, False
        
        for line in matrix:
            idx, found = search(line, 0, n-1, target)
            if True == found:
                return True
        return False

    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        def search(nums, num):
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = (l + r)//2
                if nums[m] == num:
                    return True
                if nums[m] > num:
                    r = m - 1
                else:
                    l = m + 1

            return False

        for line in matrix:
            if search(line, target):
                return True
        return False
            
            
stime = time.time()
print(Solution().searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 5))
print('elapse time: {} sec'.format(time.time() - stime))

     