import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def duplicateZeros(self, arr: [int]) -> None:
        n = len(arr)
        zeros = arr.count(0)
        
        i = n - 1
        while i >= 0:
            if i + zeros < n:
                arr[i + zeros] = arr[i]
                if arr[i] == 0:
                    if i + zeros - 1 >= 0:
                        arr[i + zeros - 1] = 0
                        zeros -= 1
            elif arr[i] == 0:
                zeros -= 1
            else:
                arr[i] = 0
            i -= 1

        return arr

    def duplicateZeros(self, arr: [int]) -> None:
        n = len(arr)
        zeros = arr.count(0)

        i = n - 1

        while i >= 0:
            if i + zeros < n:
                arr[i + zeros] = arr[i]
                if arr[i] == 0 and i + zeros - 1 >= 0:
                    zeros -= 1
                    arr[i + zeros] = 0
            elif arr[i] == 0:
                zeros -= 1
            else:
                arr[i] = 0
            i -= 1

        return arr


stime = time.time()
#print([1,0,0,2,3,0,0,4] == Solution().duplicateZeros([1,0,2,3,0,4,5,0]))
print([0,0,1,7,6,0,0,2] == Solution().duplicateZeros([0,1,7,6,0,2,0,7]))
#print([8,4,5,0,0,0,0,0] == Solution().duplicateZeros([8,4,5,0,0,0,0,7]))
print('elapse time: {} sec'.format(time.time() - stime))