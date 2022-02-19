import time


# 1. "a" , dfs("ab") -> "a","a",dfs("b") -> "a","a","b"
# 2. "aa",dfs("b")
# ...

class Solution:
    def partition(self, s: str):
        def dfs(s, seq, res):
            if not s:
                res += seq,
                return
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:], seq + [s[:i]], res)

        res = []
        dfs(s, [], res)
        return res

    def get_palindrome_partitions(self, s: str):
        def permutate(s, seq, res):
            if not s:
                res += seq,
                return

            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    permutate(s[i:], seq + [s[:i]], res)

        res = []
        permutate(s, [], res)
        return res

    def get_palindrome_partitions(self, s: str):
        res = []
        stk = [(s, [])]
        
        while stk:
            nstk = []

            while stk:
                s, seq = stk.pop()
                if not s:
                    res += seq,
                    continue

                for i in range(1, len(s) + 1):
                    if s[:i] == s[:i][::-1]:
                        nstk += (s[i:], seq + [s[:i]]),

            stk = nstk

        return res



stime = time.time()
print(Solution().partition("uoupp"))
# print([['a', 'b', 'c'], ['aa', 'b']] == Solution().partition("aab"))
# print([['a']] == Solution().partition("a"))
print('elapse time: {} sec'.format(time.time() - stime))