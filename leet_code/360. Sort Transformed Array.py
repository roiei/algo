
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        arr = nums
        n = len(nums)

        for i in range(n):
            arr[i] = a*arr[i]**2 + b*arr[i] + c

        index = -1
        maximum = float('-inf')
          
        # Find maximum element in 
        # resultant array 
        for i in range(n): 
            if maximum < arr[i]: 
                index = i 
                maximum = arr[i] 
          
        # Use maximum element as a break point  
        # and merge both subarrays usin simple  
        # merge function of merge sort  
        i = 0; j = n - 1; 
        new_arr = [0]*n 
        k = 0
        while i < index and j > index: 
            if arr[i] < arr[j]: 
                new_arr[k] = arr[i] 
                k += 1
                i += 1
            else: 
                new_arr[k] = arr[j] 
                k += 1
                j -= 1
      
        # Merge remaining elements  
        while i < index: 
            new_arr[k] = arr[i] 
            k += 1
            i += 1
      
        # Modify original array  
        while j > index: 
            new_arr[k] = arr[j] 
            k += 1
            j -= 1
            new_arr[n - 1] = maximum  
      
        for i in range(n): 
            arr[i] = new_arr[i] 

        print(arr)
        return arr


        
                    


stime = time.time()
print([3, 9, 15, 33] == Solution().sortTransformedArray(nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5))
print('elapse time: {} sec'.format(time.time() - stime))