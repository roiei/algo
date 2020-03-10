

class Solution:
    def removeDuplicates(self, S: str) -> str:
        if '' == S:
            return ''
        s = list(S)
        i = 1
        while True:
            if i >= len(s) or len(s) < 2:
                break
            if s[i-1] == s[i]:
                s.pop(i)
                s.pop(i-1)
                if i > 1:
                    i -= 1
                continue
            i += 1
        if len(s) == 2:
            if s[0] == s[1]:
                return ''
        return ''.join(s)


    def removeDuplicates(self, S: str) -> str:
        if '' == S:
            return ''
        res = ''
        for ch in S:
            if res:
                res += ch
                if res[-1] == res[-2]:
                    res = res[0:-2]
            else:
                res += ch
        return res

