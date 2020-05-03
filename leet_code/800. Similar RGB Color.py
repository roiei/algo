import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    """
    @param color: the given color
    @return: a 7 character color that is most similar to the given color
    """
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        def getClosest(s):
            m = ['00','11','22','33','44','55','66','77','88','99','aa','bb','cc','dd','ee','ff']
            return min(m, key = lambda x: abs(int(x, 16)- int(s,16)))
        
        res = ''
        color = color[1:]
        for i in range(3):
            s = color[2*i:2*i+2]
            res += getClosest(s)
        return '#' +res
    
    
    def similarRGB(self, color):
        res = []
        for i in range(1, len(color), 2):
            clr = color[i:i + 2]
            mn = float('inf')
            
            for j in range(16):
                comp_clr = hex(j)
                comp_clr = '0x' + comp_clr[2:]*2

                diff = abs(int(clr, 16) - int(comp_clr, 16))
                
                if mn > diff:
                    mn = diff
                    mn_clr = comp_clr[2:]
                    
            res += mn_clr,
        
        return '#' + ''.join(res)


stime = time.time()
print("#11ee66"== Solution().similarRGB("#09f166"))
print('elapse time: {} sec'.format(time.time() - stime))
