import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def lcs(word1, word2, m, n):
            if (m == 0 or n == 0):
                return 0;
            if (word1[m-1] == word2[n-1]):
                return 1 + lcs(word1, word2, m-1, n-1);
            else:
                return max(lcs(word1, word2, m, n-1), lcs(word1, word2, m-1, n));

        m = len(word1)
        n = len(word2)
        len_lcs = lcs(word1, word2, m, n)
        return m + n - len_lcs*2

    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if '' == word1 or '' == word2:
            return max(n, m)
        cache = {}
        def lcs(word1, i, m, word2, j, n):
            if i == m or j == n:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            length = 0
            if word1[i] == word2[j]:
                length = 1 + lcs(word1, i+1, m, word2, j+1, n)
            else:
                length = max(lcs(word1, i+1, m, word2, j, n), lcs(word1, i, m, word2, j+1, n))
            cache[(i, j)] = length
            return length
        
        len_lcs = lcs(word1, 0, m, word2, 0, n)
        return (n-len_lcs)+(m-len_lcs)

    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        def dfs(i, j):
            if (i, j) in mem:
                return mem[(i, j)]

            if i == m or j == n:
                return 0

            res = 0
            if word1[i] == word2[j]:
                res = dfs(i + 1, j + 1) + 1
            else:
                res = max(dfs(i + 1, j), dfs(i, j + 1))

            mem[(i, j)] = res
            return res

        mem = {}
        len_common = dfs(0, 0)
        return (m - len_common) + (n - len_common)

    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0]*(n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return (m - dp[-1][-1]) + (n - dp[-1][-1])


stime = time.time()
print(2 == Solution().minDistance("sea", "eat"))
print(4 == Solution().minDistance("sea", "ate"))
print(2 == Solution().minDistance("sea", "soa"))
print(1 == Solution().minDistance("a", "ab"))
print(1 == Solution().minDistance("ab", "a"))
print(7 == Solution().minDistance("food", "money"))
print('elapse time: {} sec'.format(time.time() - stime))