import time


class Solution:
    def __init__(self):
        self.dirs = {}
        self.dirs['U'] = [ 1,  0]
        self.dirs['D'] = [-1,  0]
        self.dirs['L'] = [ 0, -1]
        self.dirs['R'] = [ 0,  1]

    def judgeCircle(self, moves: str) -> bool:
        ix = iy = sx = sy = 0
        for m in moves:
            sy += self.dirs[m][0]
            sx += self.dirs[m][1]
        return True if iy == sy and ix == sx else False


stime = time.time()
r = Solution().judgeCircle('UD')
print(r)
print('elapse time: {} sec'.format(time.time() - stime))

