class Solution:
    def firstBadVersion(self, n):
        if 0 == n:
            return 0
        l = 0;r = n
        while l <= r:
            m = (l+r)//2
            if True == isBadVersion(m):
                if False == isBadVersion(m-1):
                    return m
                r = m-1
            else:
                l = m+1
        return -1
