class Solution:
    def addDigits(self, num: int) -> int:
        tot = sum([int(n) for n in str(num)])
        tot = sum([int(n) for n in str(tot)])
        return tot if tot < 10 else sum([int(n) for n in str(tot)])

