class Solution:
    def __init__(self):
        self.uprimes = [2, 3, 5]

    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        while num > 1:
            pre_num = num
            for uprime in self.uprimes:
                if 0 == num%uprime:
                    num //= uprime
            if pre_num == num:
                return False
        return True if 1 == num else False

stime = time.time()
sol = Solution()
print(sol.isUgly(6)) # True
print(sol.isUgly(14)) # True
print('elapse time: {} sec'.format(time.time() - stime))