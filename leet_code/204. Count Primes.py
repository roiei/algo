
import time
import copy
import collections


class Solution(object):
    # sieve of Eratosthenes
    def countPrimes(self, n):
        dp = [False]*n
        cnt = 0
        
        for i in range(2, n):
            if dp[i] == False:                
                step = 1
                while i*step < n:
                    dp[i*step] = True
                    step += 1
                
                cnt += 1
        
        return cnt


    def countPrimes(self, n):
        cnt = 0
        sieve = [True]*n

        for i in range(2, n):
            if sieve[i]:
                cnt += 1
                for j in range(i*i, n, i):
                    sieve[j] = False
        return cnt

    
        

stime = time.time()
print(4 == Solution().countPrimes(10))
print('elapse time: {} sec'.format(time.time() - stime))