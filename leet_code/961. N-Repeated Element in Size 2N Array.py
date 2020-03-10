class Solution:
    def repeatedNTimes(self, A: [int]) -> int:
        if not A:
            return 0
        n = len(A)
        n //= 2
        count = {}
        for a in A:
            if a not in count:
                count[a] = 0
            count[a] += 1
        count = sorted(count.items(), key=lambda p:p[1], reverse=True)
        for cnt in count:
            if cnt[1] == n:
                return cnt[0]
        return -1
            
print('{:02}'.format(1))