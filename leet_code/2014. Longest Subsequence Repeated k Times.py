
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List
from itertools import permutations
from itertools import combinations



class Solution:
    def isSubsequence(self, s, t):
        t = iter(t)
        return all(c in t for c in s)

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        hot = "".join(el*(freq//k) for el, freq in collections.Counter(s).items())

        combs = set()
        for l in range(len(hot) + 1):
            for cand in combinations(hot, l):
                for perm in permutations(cand):
                    combs.add("".join(perm))

        combs = sorted(combs, key=lambda p: (len(p), p), reverse=True)

        for c in combs:
            if self.isSubsequence(c*k, s):
                return c

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        filtered = "".join(el*(freq//k) for el, freq in collections.Counter(s).items())

        def dfs(n, sel, seq, res):
            if len(seq) == n:
                res.add(''.join(seq))
                return

            for i in range(len(filtered)):
                if i in sel:
                    continue

                dfs(n, sel + [i], seq + [filtered[i]], res)

        def is_subseq(sub, seq):
            seq = iter(seq)
            return all(c in seq for c in sub)

        combs = set()
        for i in range(1, len(filtered) + 1):
            dfs(i, [], [], combs)

        combs = sorted(combs, key=lambda p: (len(p), p), reverse=True)

        for c in combs:
            if is_subseq(c*k, s):
                return c

        return ''


stime = time.time()
print("let" == Solution().longestSubsequenceRepeatedK(s = "letsleetcode", k = 2))
print('elapse time: {} sec'.format(time.time() - stime))