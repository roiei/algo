
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def reformat(self, s: str) -> str:
        nums = []
        chs = []
        
        for ch in s:
            if ch.isalpha():
                chs += ch,
            else:
                nums += ch,
        
        res = ''
        toggle = True

        if abs(len(nums) - len(chs)) > 1:
            return ""

        if len(chs) >= len(nums):
            first, second = chs, nums
        else:
            first, second = nums, chs

        while first or second:
            if toggle and first:
                res += first.pop(0)
            elif second:
                res += second.pop(0)

            toggle = not toggle
        
        return res



stime = time.time()
print('elapse time: {} sec'.format(time.time() - stime))