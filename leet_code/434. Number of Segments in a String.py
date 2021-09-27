import time
from util.util_list import *
from util.util_tree import *
import copy
import collections



class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        
        res = []
        pre = None
        item = ''
        s += ' '

        for ch in s:
            if pre != ' ' and ch == ' ':
                res += item,
                item = ''
            else:
                item += ch
            
            pre = ch
                
        return len(res)

    def countSegments(self, s: str) -> int:
        s = s.strip()
        n = len(s)        
        i  = 0
        cnt = 0
        
        while i < n:
            while i < n and s[i] != ' ':
                i += 1
            
            cnt += 1
            
            j = i
            empty_cnt = 0
            while j < n and s[j] == ' ':
                empty_cnt += 1
                j += 1

            i += empty_cnt
        
        return cnt


stime = time.time()
print(5 == Solution().countSegments("Hello, my    name is John"))
print('elapse time: {} sec'.format(time.time() - stime))