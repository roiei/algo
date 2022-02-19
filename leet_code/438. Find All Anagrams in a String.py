import time
import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> 'List[int]':
        n = len(s)
        m = len(p)
        if n < m:
            return []
        sfreq = {}
        pfreq = {}
        ptrs = []

        for i in range(m):
            if p[i] not in pfreq:
                pfreq[p[i]] = 0
            pfreq[p[i]] += 1

        for i in range(m):
            if s[i] not in sfreq:
                sfreq[s[i]] = 0
            sfreq[s[i]] += 1

        if sfreq == pfreq:
            ptrs.append(0)

        for i in range(m, n):
            sfreq[s[i-m]]-= 1
            if 0 == sfreq[s[i-m]]:
                del sfreq[s[i-m]]
            if s[i] not in sfreq:
                sfreq[s[i]] = 0
            sfreq[s[i]] += 1

            if sfreq == pfreq:
                ptrs.append(i-m+1)
        return ptrs

    def find_anagrams(self, s: str, p: str) -> [int]:
        m = len(s)
        n = len(p)
        pcnt = collections.Counter(p)
        scnt = collections.Counter(s[:n])
        res = []
        
        if pcnt == scnt:
            res += 0,
        
        for i in range(n, m):
            scnt[s[i - n]] -= 1
            if scnt[s[i - n]] == 0:
                del scnt[s[i - n]]
            
            if s[i] not in scnt:
                scnt[s[i]] = 0
            scnt[s[i]] += 1
            
            if scnt == pcnt:
                res += i - n + 1,
        
        return res

    def find_anagrams(self, s: str, p: str) -> [int]:
        def get_idx(ch):
            return ord(ch) - ord('a')

        def is_same(a, b):
            return all([False if a[i] != b[i] else True for i in range(num_alphabet)])

        m = len(s)
        n = len(p)
        if m < n:
            return []

        num_alphabet = 26
        wnd = [0]*num_alphabet
        ans = [0]*num_alphabet

        for i, ch in enumerate(p):
            ans[get_idx(ch)] += 1

        for i in range(n):
            wnd[get_idx(s[i])] += 1

        res = []
        if is_same(ans, wnd):
            res += 0,

        for i in range(n, m):
            wnd[get_idx(s[i - n])] -= 1
            wnd[get_idx(s[i])] += 1

            if is_same(ans, wnd):
                res += i - n + 1,

        return res


stime = time.time()
print(Solution().findAnagrams("pokijokpq", "kop"))
# print(Solution().findAnagrams("cbaebabacd", "abc")) # [0, 6]
# print(Solution().findAnagrams("abab", "ab")) # [0, 1, 2]
# print(Solution().findAnagrams("beeaaedcbc", "c")) #[7, 9]
print('elapse time: {} sec'.format(time.time() - stime))