class Solution:
    cnt = 0
    times = []
    def perm_dup(self, time, n, depth, trace):
        if depth == n:
            first = int(trace[0])
            second = int(trace[1])
            if 0 <= first <= 2 and (not (first == 2 and (0 <= second <= 3))):
                self.times.append(trace[::])
                self.cnt += 1
            return

        for i in range(n):
            trace.append(time[i])
            self.perm_dup(time, n, depth+1, trace)
            trace.pop()

    def next_time(self, time: str) -> int:
        time = [i for i in time if i != ':']
        self.perm_dup(time, len(time), 0, [])
        return self.get_closest(time)

    def convert_min(self, time):
        minite = int(time[0])*10*60 + int(time[1])*60 + int(time[2])*10 + int(time[3])
        return minite

    def convert_strhour(self, vals):
        hours = vals//60
        minute = vals%60
        return '{:02}:{:02}'.format(hours, minute)

    def get_closest(self, base):
        b = self.convert_min(base)
        pos_diffs = []
        neg_diffs = []
        for t in self.times:
            diff = self.convert_min(t) - b
            if diff < 0:
                neg_diffs.append(diff)
            else:
                if diff != 0:
                    pos_diffs.append(diff)
        
        neg_diffs.sort(reverse=True)
        pos_diffs.sort()

        closest = pos_diffs[0]
        if not pos_diffs:
            closest = neg_diffs[-1]

        return self.convert_strhour(b + closest)

    def print_times(self):
        for t in self.times:
            print(t)

time = "17:31"

sol = Solution()
ret = sol.next_time(time)
print(ret)