import time


class Solution:
    def get_palindrome_substr(self, s, n, r, depth, start, trace, res):
        if depth == r:
            t = ''.join([v[0] for v in trace])            
            if t == t[::-1]:
                idxs = [v[1] for v in trace]
                idxs.sort()
                invalid = False
                for i in range(len(idxs)-1):
                    if 1 < idxs[i+1]-idxs[i]:
                        invalid = True
                        break
                if False == invalid:
                    res.append(''.join(t[:]))
            return
        for i in range(start, n):
            trace.append([s[i], i])
            self.get_palindrome_substr(s, n, r, depth+1, i+1, trace, res)
            trace.pop()

    def countSubstrings_es(self, s: str) -> int:
        n = len(s)
        res = []
        for r in range(1, n+1):
            self.get_palindrome_substr(s, n, r, 0, 0, [], res)
        return len(res)

    def countSubstrings(self, s):
        n = len(s)
        steps = [1 for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    steps[i] += 1
        return sum(steps)
        


stime = time.time()
#print(Solution().countSubstrings("abc")) # "a", "b", "c".
print(Solution().countSubstrings("aaa"))
print(Solution().countSubstrings("abcda"))
print(Solution().countSubstrings("abad"))
print('elapse time: {} sec'.format(time.time() - stime))