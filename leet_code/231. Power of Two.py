class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 1
        val = 1
        while val < n:
            val = int(bin(1<<i), 2)
            i+= 1

        if val == n:
            return True
        return False

n = 1
#n = 16

sol = Solution()
ret = sol.isPowerOfTwo(n)
print(ret)
