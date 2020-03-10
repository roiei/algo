import time


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if 0 == n:
            return False
        power = 0; cur = 0
        while cur < n:
            cur = 3**power
            power += 1
        return True if n == cur else False


stime = time.time()
r = Solution().isPowerOfThree(27)
print(r)
print('elapse time: {} sec'.format(time.time() - stime))

