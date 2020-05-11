
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def primePalindrome(self, N: int) -> int:
        def isPrime(x):
            if x < 2 or x%2 == 0:
                return x == 2
            
            for i in range(3, int(x**0.5) + 1):
                if x%i == 0:
                    return False
                
            return True
        
        if 8 <= N <= 11:
            return 11

        # len(N) == 1 -> 10**0 == 1
        # len(N) == 2 -> 10**1 == 10
        # len(N) == 3 -> 10**1 == 10
        # len(N) == 4 -> 10**2 == 100
        # ...

        for x in range(10**(len(str(N))//2), 10**8):
            x = str(x)
            palindrome = int(x + x[-2::-1])
            if palindrome >= N and isPrime(palindrome):
                return palindrome

    def primePalindrome(self, N: int) -> int:
        def isPrime(num):
            if num == 2:
                return True
            
            if num < 2 or num%2 == 0:
                return False

            for i in range(3, int(num**0.5) + 1, 2):
                if num%i == 0:
                    break
            else:
                return True
                
            return False
        
        #for x in range(10**(len(str(N)) // 2), 10**8):
        for x in range(1, 10**8):
            x = str(x)
            palindrome = int(x + x[:-1][::-1])
            print(palindrome)
            if palindrome >= N and isPrime(palindrome):
                print(palindrome)
                return palindrome
            print()
        

stime = time.time()
#print(7 == Solution().primePalindrome(6))
#print(Solution().primePalindrome(102))
#print(Solution().primePalindrome(132))
print(11 == Solution().primePalindrome(8))
#print(101 == Solution().primePalindrome(13))
print('elapse time: {} sec'.format(time.time() - stime))