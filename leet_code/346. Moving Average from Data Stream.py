

class Solution:
    wnd_size = 0
    n = 0
    vals = []
    def do_moving_avg(self, wnd_size):
        self.wnd_size = wnd_size

    def next(self, val):
        if self.n >= self.wnd_size:
            self.vals.pop(0)
            self.n -= 1
        self.vals.append(val)
        self.n += 1
        return sum(self.vals) / self.n
        

wnd_size = 3
vals = [1, 10, 3, 5]

sol = Solution()
sol.do_moving_avg(wnd_size)
print(sol.next(1))
print(sol.next(10))
print(sol.next(3))
print(sol.next(5))