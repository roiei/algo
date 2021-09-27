import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str):
        addr = s
        
        def dfs(addr, seq, res):
            if not addr or len(seq) == 4:
                if not addr and len(seq) == 4:
                    res += '.'.join(seq),
                return

            if addr[0] == '0':
                dfs(addr[1:], seq + ['0'], res)
                return

            for i in range(1, len(addr) + 1):
                if int(addr[:i]) > 255:
                    break

                dfs(addr[i:], seq + [addr[:i]], res)

        res = []
        dfs(addr, [], res)
        return res

    def restoreIpAddresses2(self, s: str) -> List[str]:
        addr = s
        n = len(addr)
        
        def dfs(start, seq, res):
            if start == n or len(seq) == 4:
                if start == n and len(seq) == 4:
                    res += '.'.join(seq),
                return

            if addr[start] == '0':
                dfs(start + 1, seq + ['0'], res)
                return

            for i in range(start + 1, len(addr) + 1):
                if int(addr[start:i]) > 255:
                    break
                    
                dfs(start + i, seq +[addr[start:i]], res)

        res = []
        dfs(0, [], res)
        return res

    def restoreIpAddresses(self, s: str) -> List[str]:
        addr = s
        n = len(addr)
        
        def dfs(start, seq, res):
            if start == n or len(seq) == 4:
                if start == n and len(seq) == 4:
                    res += '.'.join(seq),
                return
        
            if addr[start] == '0':
                dfs(start + 1, seq + [addr[start]], res)
                return
        
            for i in range(start, n):
                if int(addr[start:i + 1]) > 255:
                    break

                dfs(i + 1, seq + [addr[start:i + 1]], res)
        
        res = []
        dfs(0, [], res)
        return res


# ["255.255.11.135","255.255.111.35","255.255.1113.5"]
# ["255.255.11.135","255.255.111.35"]

stime = time.time()
#print(Solution().restoreIpAddresses('0000'))
# 255 255 111 35
# 255 255 11 135
print(Solution().restoreIpAddresses("25525511135"))
print('elapse time: {} sec'.format(time.time() - stime))