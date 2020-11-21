
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def countGroups(self, emails):
        uniq = collections.defaultdict(int)
        
        for email in emails:
            acc, domain = email.split('@')
            
            idx = acc.find('+')
            if idx != -1:
                acc = acc[:idx]
            acc = ''.join([ch for ch in acc if ch != '.'])
            key = acc + '@' + domain
            uniq[key] += 1
        
        return len([key for key, value in uniq.items() if value > 1])


stime = time.time()
print(1 == Solution().countGroups(["abc.bc+c+d@jiuzhang.com", "abcbc+d@jiuzhang.com", "abc.bc.cd@jiuzhang.com"]))
print('elapse time: {} sec'.format(time.time() - stime))