class Solution:
    def totalMoney(self, n: int) -> int:
        aweek_tot = sum([i for i in range(1, 8)])
        weeks = n//7
        days = n%7

        weight = 0
        tot = 0

        for week in range(weeks):
            tot += aweek_tot + weight*7
            weight += 1

        for day in range(1, days + 1):
            tot += day + weight

        return tot
