import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def numberOfLines(self, widths: [int], S: str) -> [int]:
        if not widths:
            return None
        
        ch_len = collections.defaultdict(int)
        cnt = 'a'
        for i, width in enumerate(widths):
            ch_len[cnt] = width
            cnt = chr(ord(cnt) + 1)
            
        ONE_LINE = 100
        line = 1
        left = ONE_LINE
        filled = 0
        for s in S:
            if left < ch_len[s]:
                left = ONE_LINE
                line += 1
                filled = 0

            if left >= ch_len[s]:
                left -= ch_len[s]
                filled += ch_len[s]
                
        return [line, filled]
            

stime = time.time()
print([3, 60] == Solution().numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz"))
print('elapse time: {} sec'.format(time.time() - stime))