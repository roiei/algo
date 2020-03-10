
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findMaxForm(self, strs: [str], m: int, n: int) -> int:
        
        def recur(start, m, n, cnt):
            #if start in mem and cnt < mem[start]:
            #    return mem[start]
            
            if start == len(strs):
                return cnt
            
            res = []
            for i in range(start, len(strs)):
                zeros = strs[i].count('0')
                ones = strs[i].count('1')
                if zeros <= m and ones <= n:
                    res += recur(i + 1, m - zeros, n - ones, cnt + 1),
                else:
                    res += recur(i + 1, m, n, cnt),

            #print('start = {}, res = {}'.format(start, res))
            
            mem[start] = max(res)
            return mem[start]
    
        mem = {}
        return recur(0, m, n, 0)


stime = time.time()
#print(4 == Solution().findMaxForm(strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3))
#print(2 == Solution().findMaxForm(strs = ["10", "0", "1"], m = 1, n = 1))
print(17 == Solution().findMaxForm(["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"], 9, 80))
print('elapse time: {} sec'.format(time.time() - stime))