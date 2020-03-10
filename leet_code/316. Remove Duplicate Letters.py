import time


class Solution:
    def get_uniq(self, s, start, n, depth, uniq, res):
        idx = ''.join(uniq)
        if idx in self.mem:
            return
        if start == n:
            if idx not in self.mem:
                self.mem[idx] = True
            res.append([idx, len(uniq)])
            return
        for i in range(start, n):
            pushed = False
            if s[i] not in uniq:
                pushed = True
                uniq.append(s[i])
            self.get_uniq(s, i+1, n, depth+1, uniq, res)
            if True == pushed:
                uniq.pop()

    def removeDuplicateLetters_es(self, s: str) -> str:
        if not s:
            return ''
        self.mem = {}
        n = len(s)
        res = []
        self.get_uniq(s, 0, n, 0, [], res)
        print(res)
        res.sort(key=lambda param:param[1], reverse=True)
        ml = res[0][1]
        res = [r[0] for r in res if r[1] == ml]
        res.sort()
        return res[0]

    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) <= 1:
            return s
        S = set(s)
        cnt = list(S)
        cnt.sort()
        cnt.reverse()
        find = False
        cur = ''
        i = -1
        while cnt and find is False:
            cur = cnt.pop() # get the head of the substring
            i = s.index(cur)
            for j, item in enumerate(s[:i]):
                if item not in s[i:]:
                    break
                if j == i-1:
                    find = True
            if i == 0:
                break
        return cur + self.removeDuplicateLetters(s[i:].replace(cur, ''))

stime = time.time()
# print(Solution().removeDuplicateLetters("bcabc")) # abc
# print(Solution().removeDuplicateLetters("cbacdcbc")) # acdb
print(Solution().removeDuplicateLetters_es("bbcaac")) # bac
print(Solution().removeDuplicateLetters("bbcaac")) # bac
#print(Solution().removeDuplicateLetters("thesqtitxyetpxloeevdeqifkz")) 
print('elapse time: {} sec'.format(time.time() - stime))