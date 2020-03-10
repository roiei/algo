
import time

class Solution:
    def monotoneIncreasingDigits_es(self, N: int) -> int:
        largest = 0
        for i in range(N+1):
            cur = str(i)
            okay = True
            for j in range(len(cur)-1):
                if cur[j] > cur[j+1]:
                    okay = False
            if True == okay:
                if largest < i:
                    largest = i
        return largest

    def is_monotonic_inc(self, num):
        num = str(num)
        for j in range(len(num)-1):
            if num[j] > num[j+1]:
                return False
        return True

    def monotoneIncreasingDigits(self, N: int) -> int:
        num = str(N)
        prev = '0'
        while True:
            n = len(num)
            for i in range(n-1):
                if num[i] > num[i+1]:
                    num = str(int(num[:i+1])-1) + '9'*(n-i-1)
            if prev == num:
                break
            prev = num[:]
        return int(num)
        

stime = time.time()
sol = Solution()
print(sol.monotoneIncreasingDigits(10))
print(sol.monotoneIncreasingDigits(1234))
print(sol.monotoneIncreasingDigits(332))
print('elapse time: {} sec'.format(time.time() - stime))