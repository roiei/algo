
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def maxLength(self, arr: [str]) -> int:
        n = len(arr)
        if n == 1:
            return len(arr[0])

        def dfs(start, seq, mx):
            if start == n:
                return
        
            for i in range(start, n):
                comm = set(seq)|set(arr[i])
                if len(comm) == len(seq) + len(arr[i]):
                    mx[0] = max(mx[0], len(comm))
                    dfs(i + 1, seq + arr[i], mx)
        
        mx = [0]
        dfs(0, '', mx)
        return mx[0]


stime = time.time()
# print(4 == Solution().maxLength(["un","iq","ue"]))
# print(26 == Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]))
print(16 == Solution().maxLength(["jnfbyktlrqumowxd","mvhgcpxnjzrdei"]))
print('elapse time: {} sec'.format(time.time() - stime))