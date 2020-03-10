

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if not A:
            return 0
        l = 0
        r = len(A)-1
        while l <= r:
            m = (l+r)//2
            if A[m-1] < A[m] > A[m+1]:
                return m
            if A[m-1] < A[m+1]:
                l = m+1
            else:
                r = m-1
