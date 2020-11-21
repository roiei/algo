import time


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
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
# print(Solution().removeDuplicateLetters("bcabc")) # abc

#print(Solution().removeDuplicateLetters("cba")) # acdb
print('acdb' == Solution().removeDuplicateLetters("cbacdcbc")) # acdb

#    abcd
#    bcd
#    bd

print('bac' == Solution().removeDuplicateLetters("bbcaac")) # bac
print('bac' == Solution().removeDuplicateLetters("bbcaac")) # bac
#print(Solution().removeDuplicateLetters("thesqtitxyetpxloeevdeqifkz")) 
print('elapse time: {} sec'.format(time.time() - stime))