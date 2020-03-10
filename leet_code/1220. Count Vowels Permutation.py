import time
import copy
import collections
import heapq


class Solution(object):

    # timeout
    def countVowelPermutation(self, n):
        q = list(zip(['a', 'e', 'i', 'o', 'u'], [1]*5))
        cnt = 0
        
        while q:
            ch, level = q.pop(0)
            if level == n:
                cnt += 1
            if level + 1 > n:
                continue
            
            if ch == 'a':
                q += ('e', level + 1),
            elif ch == 'e':
                q += ('a', level + 1),
                q += ('i', level + 1),
            elif ch == 'i':
                q += ('a', level + 1),
                q += ('e', level + 1),
                q += ('o', level + 1),
                q += ('u', level + 1),
            elif ch == 'o':
                q += ('i', level + 1),
                q += ('u', level + 1),
            elif ch == 'u':
                q += ('a', level + 1),
        
        return cnt


    def countVowelPermutation(self, n):
        dp = [[0]*5 for _ in range(n)]
        for i in range(5):
            dp[0][i] = 1

        for i in range(1, n):
            for j in range(5):
                if j == 0: # 'a'
                    dp[i][j + 1] += dp[i - 1][j]
                elif j == 1: # 'e'
                    dp[i][j - 1] += dp[i - 1][j]
                    dp[i][j + 1] += dp[i - 1][j]
                elif j == 2: # 'i'
                    dp[i][j - 2] += dp[i - 1][j]
                    dp[i][j - 1] += dp[i - 1][j]
                    dp[i][j + 1] += dp[i - 1][j]
                    dp[i][j + 2] += dp[i - 1][j]
                elif j == 3:
                    dp[i][j - 1] += dp[i - 1][j]
                    dp[i][j + 1] += dp[i - 1][j]
                elif j == 4:
                    dp[i][j - 4] += dp[i - 1][j]

        tot = sum(dp[-1])
        tot = tot%(10**9 + 7)
        return tot


stime = time.time()
print(10 == Solution().countVowelPermutation(2))
print(Solution().countVowelPermutation(3))
print(Solution().countVowelPermutation(4))
print(68 == Solution().countVowelPermutation(5))
print(Solution().countVowelPermutation(144))
print('elapse time: {} sec'.format(time.time() - stime))


