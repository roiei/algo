
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List
import math



class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        
        def dfs(start, seq, idxs, res):
            if start == n:
                if seq == seq[::-1]:
                    key = tuple(sorted(idxs))
                    res[key] = max(res[key], len(seq))
                return
            
            for i in range(start, n):
                dfs(i + 1, seq + [s[i]], idxs + [i], res)
                dfs(i + 1, seq, idxs, res)
        
        res = collections.defaultdict(int)
        dfs(0, [], [], res)

        res = sorted(res.items(), key=lambda p: p[1], reverse=True)
        mx = 0

        for i in range(len(res) - 1):
            for j in range(i + 1, len(res)):
                if set(res[i][0]) & set(res[j][0]):
                    continue

                if 0 == res[i][1] or 0 == res[j][1]:
                    continue

                mx = max(mx, res[i][1]*res[j][1])

        return mx

    def maxProduct(self, s: str) -> int:
        n = len(s)
        mx = [0]

        def dfs(seq1, seq2, start, mx):
            cur_key = tuple([seq1, seq2, start])
            if cur_key in visited:
                return

            if seq1 == seq1[::-1] and seq2 == seq2[::-1]:
                mx[0] = max(mx[0], len(seq1)*len(seq2))

            visited.add(cur_key)

            if start == n:
                return

            dfs(seq1 + s[start], seq2, start + 1, mx)
            dfs(seq1, seq2 + s[start], start + 1, mx)
            dfs(seq1, seq2, start + 1, mx)

        visited = set()
        dfs('', '', 0, mx)
        return mx[0]


stime = time.time()
print(9 == Solution().maxProduct(s = "leetcodecom"))
print(1 == Solution().maxProduct(s = "bb"))
print(25 == Solution().maxProduct(s = "accbcaxxcxx"))
print(4 == Solution().maxProduct(s = "ueeu"))
print('elapse time: {} sec'.format(time.time() - stime))