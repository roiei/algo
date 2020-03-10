import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def restoreIpAddresses(self, s: str) -> 'List[str]':
        if "" == s:
            return []
        n = len(s)
        pad = 0
        while 0 != (n+pad)%4:
            pad += 1
        step = (n+pad)//4
        print(step, pad, n)
        
        ip = []
        for i in range(2):
            ip += s[i*step:(i+1)*step],
        print('ip = ', ip)
        res = []
        start = step*2

        print('step = {}, start = {} pad = {}'.format(step, start, pad))
        cnt = 0
        for i in range((step*2-pad)//2, step*2-pad):
            if 2 == cnt:
                break
            print(ip)
            print(s[start:start+i])
            print(s[start+i:])
            res += ip + [s[start:start+i]] + [s[start+i:]],
            cnt += 1
        return ['.'.join(r) for r in res]

# ["255.255.11.135","255.255.111.35","255.255.1113.5"]
# ["255.255.11.135","255.255.111.35"]

stime = time.time()
print(Solution().restoreIpAddresses('0000'))
print(Solution().restoreIpAddresses("25525511135"))
print('elapse time: {} sec'.format(time.time() - stime))