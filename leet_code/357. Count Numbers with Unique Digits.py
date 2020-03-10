import time


class Solution:
    def countNumbersWithUniqueDigits2(self, n: int) -> int:
        cnt = 0
        nuniq = 0
        n = 10**n
        for i in range(n):
            si = str(i)
            sn = len(si)
            uniq = [si[0]]
            for j in range(1, sn):
                if si[j] in uniq:
                    break
                uniq.append(si[j])
            if sn == len(uniq):
                cnt += 1
            else:
                nuniq += 1
        print('nuniq = ', nuniq)
        return cnt

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if 0 == n:
            return 1
        val = 10
        for i in range(n-1):
            v = 9
            for j in range(i+1):
                v *= (9-j)
            val += v
        return val

        val = 10
        for i in range(n-1):
            v = 9
            for j in range(i+1):
                v *= (9-j)
            val += v

stime = time.time()
print('2 = ', Solution().countNumbersWithUniqueDigits(2)) # 91
print('3 = ', Solution().countNumbersWithUniqueDigits(3)) # 739
print('4 = ', Solution().countNumbersWithUniqueDigits(4)) # 5275
print('5 = ', Solution().countNumbersWithUniqueDigits(5)) # 32491
print('elapse time: {} sec'.format(time.time() - stime))
