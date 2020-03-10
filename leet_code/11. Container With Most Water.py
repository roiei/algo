import time

class Solution:
    # sol 1
    def get_comb(self, xys, n, r, depth, start, trace, res):
        if r == depth:
            res.append(trace[:])
            return
        for i in range(start, n):
            trace.append(xys[i])
            self.get_comb(xys, n, r, depth+1, i+1, trace, res)
            trace.pop()

    def maxArea_es(self, height: 'List[int]') -> int:
        xys = [[i, height[i]] for i in range(len(height))]
        res = []
        self.get_comb(xys, len(xys), 2, 0, 0, [], res)
        maxval = 0
        for r in res:
            width = abs(r[0][0]-r[1][0])
            height = min(r[0][1], r[1][1])
            if width*height > maxval:
                maxval = width*height
        return maxval

    # sol 2
    mem = {}
    def get_max(self, xys, start, end):
        if start == end:
            return 0
        idx = '{}:{}'.format(start, end)
        if idx in self.mem:
            return self.mem[idx]
        res = []
        res.append(abs(xys[start][0]-xys[end][0])*min(xys[start][1], xys[end][1]))
        if start < end:
            res.append(self.get_max(xys, start+1, end))
        if start < end:
            res.append(self.get_max(xys, start, end-1))
        idx = '{}:{}'.format(start, end)
        if idx not in self.mem:
            self.mem[idx] = max(res)
        return self.mem[idx]

    def maxArea_lr(self, height: 'List[int]') -> int:
        xys = [[i, height[i]] for i in range(len(height))]
        self.mem = {}
        return self.get_max(xys, 0, len(xys)-1)

    # sol 3
    def maxArea(self, height: 'List[int]') -> int:
        xys = [[i, height[i]] for i in range(len(height))]
        start = 0
        end = len(xys)-1
        maxval = 0
        while start < end:
            maxval = max(maxval, (xys[end][0]-xys[start][0])*min(xys[start][1], xys[end][1]))
            if xys[start][1] < xys[end][1]:
                start += 1
            elif xys[start][1] > xys[end][1]:
                end -= 1
            else:
                start += 1
                end -= 1
        return maxval

stime = time.time()
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7])) # 49
print('elapse time: {} sec'.format(time.time() - stime))