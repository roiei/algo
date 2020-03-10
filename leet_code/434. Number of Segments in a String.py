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


stime = time.time()
print(5 == Solution().countSegments("Hello, my    name is John"))
print('elapse time: {} sec'.format(time.time() - stime))