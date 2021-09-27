import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        if '' == input:
            return 0
        s = input.split('\n')
        mlen = 0
        stk = []
        while s:        
            chunk = s.pop(0)
            lev = chunk.count('\t')

            while len(stk) > lev:
                stk.pop()

            chunk = chunk.replace('\t', '')
            stk += chunk,

            if '.' in chunk:
                mlen = max(mlen, len('/'.join(stk)))
        return mlen

    def lengthLongestPath(self, input: str) -> int:
        lines = input.split('\n')
        
        stk = []
        mx = 0

        for line in lines:
            depth = line.count('\t')
            
            while stk and len(stk) > depth:
                stk.pop()
            
            line = line.replace('\t', '')
            stk += line,
            
            if '.' in line:
                mx = max(mx, len('/'.join(stk)))
        
        return mx


stime = time.time()
#print(20 == Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
print(Solution().lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
print('elapse time: {} sec'.format(time.time() - stime))