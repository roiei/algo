
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    # O(N*M) algorithm -> timeout
    def canMakePaliQueries(self, s: str, queries: [[int]]) -> [bool]:
        res = []
        mem = {}

        for si, ei, k in queries:

            odd = None
            if (si, ei) in mem:
                odd = mem[(si, ei)]
            else:
                cntr = collections.Counter(s[si:ei + 1])
                odd = len([val for val in cntr.values() if val%2 != 0])
                mem[(si, ei)] = odd
            if odd >= k*2:
                odd -= k*2
            else:
                odd = 0
            if odd <= 1:
                res += True,
            else:
                res += False,
        
        return res

    def canMakePaliQueries(self, s, queries):
        dp = [collections.Counter()]
        
        for i in range(1, len(s) + 1):
            dp += dp[i - 1] + collections.Counter(s[i - 1]),
            
        res = []
        for l, r, k in queries:
            c = dp[r + 1] - dp[l]
            need = sum(v%2 for v in c.values()) // 2
            res += need <= k,
        return res

    def canMakePaliQueries(self, s, queries):
        N = 26
        a = ord('a')

        dp = [[0]*N]

        for i in range(1, len(s) + 1):
            new = dp[i - 1][:]
            j = ord(s[i - 1]) - a
            new[j] += 1
            dp += new,

        res = []
        for l, r, k in queries:
            L = dp[l]
            R = dp[r + 1]
            res += sum((R[i] - L[i])&1 for i in range(N))//2 <= k,
        return res

    def canMakePaliQueries(self, s, queries):
        
        dp = [collections.Counter()]
        
        for i, ch in enumerate(s):
            dp += dp[-1] + collections.Counter(ch),
        
        res = []
        for l, r, k in queries:
            diff = dp[r + 1] - dp[l]
            num_odd = sum(val%2 for val in diff.values()) // 2
            res += num_odd <= k,
        
        return res

    def canMakePaliQueries(self, s, queries):
        N = 26
        S = len(s) + 1
        ints = list(map(lambda c: ord(c) - ord('a'), s))

        dp = [0] * S
        for i in range(1, S):
            dp[i] = dp[i - 1] ^ (1 << ints[i - 1])

        ones = lambda x: bin(x).count('1')
        return [
            ones(dp[r + 1] ^ dp[l]) >> 1 <= k
            for l, r, k in queries
        ]
    
    def canMakePaliQueries(self, s, queries):
        N = 26
        dp = [[0]*N]
        
        for i, ch in enumerate(s):
            dp += dp[-1][:],
            dp[-1][ord(ch) - ord('a')] += 1

        res = []
        for l, r, k in queries:
            num_odd = sum((dp[r + 1][i] - dp[l][i])%2 for i in range(N))
            res += num_odd//2 <= k,
        
        return res

    def can_make_palindrome(self, s: str, requests: List[List[int]]) -> List[bool]:
        dp = [collections.Counter()]
        
        for i in range(len(s)):
            dp += dp[-1] + collections.Counter(s[i]),
        
        res = []
        for l, r, k in requests:
            req = dp[r + 1] - dp[l]
            need = sum(v%2 for v in req.values())//2
            res += need <= k,
        
        return res


stime = time.time()
#print([True,False,False,True,True] == Solution().canMakePaliQueries("abcda", [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))
print(Solution().canMakePaliQueries("zaoza", [[1,2,0],[0,3,1],[0,4,1],[2,3,1]]))
print('elapse time: {} sec'.format(time.time() - stime))