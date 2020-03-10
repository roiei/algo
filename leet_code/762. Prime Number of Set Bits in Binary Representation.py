import time

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        cnt = 0
        for num in range(L, R+1):
            num = '{:08b}'.format(num).count('1')
            if num < 2:
                continue
            is_prime = True
            for i in range(2, num//2+1):
                if num%i == 0:
                    is_prime = False
                    break
            if True == is_prime:
                cnt += 1
        return cnt


stime = time.time()
sol = Solution()
print(sol.countPrimeSetBits(6, 10))  # 4
print(sol.countPrimeSetBits(10, 15)) # 5
print('elapse time: {} sec'.format(time.time() - stime))