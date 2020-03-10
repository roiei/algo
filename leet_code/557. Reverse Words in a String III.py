
import time

class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split()
        out = []
        for s in ss:
            out.append(s[::-1])
        res = ''
        n = len(out)
        for i in range(n):
            res += out[i]
            if i < n-1:
                res += ' '
        return res

stime = time.time()
print(Solution().reverseWords("Let's take LeetCode contest"))
print('elapse time: {} sec'.format(time.time() - stime))