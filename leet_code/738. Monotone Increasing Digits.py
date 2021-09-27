
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

    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(map(int, list(str(n))))
        prev = digits[:]

        while True:
            for i in range(len(digits) - 2, -1, -1):
                if digits[i] > digits[i + 1]:
                    digits[i] -= 1
                    digits[i + 1:len(digits)] = (len(digits) - i - 1)*[9]

            while digits and digits[0] == 0:
                digits.pop(0)

            if prev == digits:
                break

            prev = digits[:]

        return ''.join(list(map(str, digits)))
        

stime = time.time()
sol = Solution()
print('99' == sol.monotoneIncreasingDigits(100))
# print('9' == sol.monotoneIncreasingDigits(10))
# print('1234' == sol.monotoneIncreasingDigits(1234))
print('299' == sol.monotoneIncreasingDigits(332))
print('elapse time: {} sec'.format(time.time() - stime))