
class Solution:
    def binaryGap(self, N: int) -> int:
        s = list('{:b}'.format(N))
        dist = 0
        mdist = 0
        for ch in s:
            if ch == '1':
                mdist = max(dist, mdist)
                dist = 0
            else:
                dist += 1
        if 1 == s.count('1'):
            return 0
        return mdist+1
