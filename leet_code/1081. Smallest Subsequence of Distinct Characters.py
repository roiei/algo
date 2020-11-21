import time


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        kind = sorted(list(set(s)))
        s = list(s)
        res = ''

        while kind:
            ch = kind.pop(0)
            idx = s.index(ch)
            
            not_find = False
            for i in range(idx):
                if s[i] not in s[i + 1:]:
                    not_find = True
                    break
            
            if not not_find:
                res += ch
                s = s[idx + 1:]

                while s and ch in s:
                    s.remove(ch)

                kind = sorted(list(set(s)))

        return res


stime = time.time()
print('abc' == Solution().smallestSubsequence("bcabc"))
print('acdb' == Solution().smallestSubsequence("cbacdcbc"))
print('elapse time: {} sec'.format(time.time() - stime))