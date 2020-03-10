
import time

class Solution:
    def findContentChildren(self, g, s) -> int:
        cnt = 0
        if not g or not s:
            return 0
        gl = len(g)
        sl = len(s)
        g.sort(reverse=True)
        s.sort(reverse=True)
        i = 0
        j = 0
        while i < gl and j < sl:
            if g[i] <= s[j]:
                j+= 1
                cnt+= 1
            i+= 1
        return cnt   


stime = time.time()
sol = Solution()
res = sol.findContentChildren([10,9,8,7],[5,6,7,8])
print(res)
print('elapse time: {} sec'.format(time.time() - stime))
