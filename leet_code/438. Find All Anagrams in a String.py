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

    def findAnagrams(self, s: str, p: str) -> [int]:
        ls = len(s)
        lp = len(p)
        pcnt = collections.Counter(p)
        scnt = collections.Counter(s[:lp])
        res = []
        
        if pcnt == scnt:
            res += 0,
        
        for i in range(lp, ls):
            scnt[s[i - lp]] -= 1
            if scnt[s[i - lp]] == 0:
                del scnt[s[i - lp]]
            
            if s[i] not in scnt:
                scnt[s[i]] = 0
            scnt[s[i]] += 1
            
            if scnt == pcnt:
                res += i - lp + 1,
        
        return res

stime = time.time()
print(Solution().findAnagrams("cbaebabacd", "abc")) # [0, 6]
# print(Solution().findAnagrams("abab", "ab")) # [0, 1, 2]
# print(Solution().findAnagrams("beeaaedcbc", "c")) #[7, 9]
print('elapse time: {} sec'.format(time.time() - stime))