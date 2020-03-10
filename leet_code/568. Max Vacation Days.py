class Solution:
    nums = 0
    def get_combs(self, ranges, n, depth, trace, skip, cases):
        if n == depth:
            self.nums+= 1
            if trace[0] == 0:
                cases.append(trace[:])
            return

        for i in range(n):
            if i in skip:
                continue
            skip.append(i)
            trace.append(ranges[i])
            self.get_combs(ranges, n, depth+1, trace, skip, cases)
            trace.pop()
            skip.pop()

    def do_get_combs(self, days):
        n = len(days)
        cases = []
        ranges = [i for i in range(n)]
        self.get_combs(ranges, n, 0, [], [], cases)
        return cases

    def get_days(self, days, flights, case):
        num_days = 0
        i = 0
        q = []
        q.append(case[0])

        num_days += days[case[i]][i]    # 1st day in city case[i]
        not_possible = False
        i += 1

        while q and i < 3:
            cur = q.pop(0)
            if 1 != flights[cur][case[i]]:
                not_possible = True
                break
            num_days += days[case[i]][i]
            #print('num_days = ', num_days)
            q.append(case[i])
            i+= 1
        if True == not_possible:
            num_days *= (3-i)
        return num_days

    def do_flight(self, days, flights, cases):
        num_days = []
        for case in cases:
            num_days.append(self.get_days(days, flights, case))
        return max(num_days)

flights = [
    [0,1,1],
    [1,0,1],
    [1,1,0]]
days = [
    [1,3,1],
    [6,0,3],
    [3,3,3]]
