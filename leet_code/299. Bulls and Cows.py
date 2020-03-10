import time
from util.util_list import *
from util.util_tree import *
import copy
import collections



class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret = list(secret)
        guess = list(guess)

        m = len(secret)
        n = len(guess)

        pos = []
        bulls = 0
        for i in range(n):
            if secret[i] == guess[i]:
                pos += i,
                bulls += 1

        while pos:
            idx = pos.pop()
            secret.pop(idx)
            guess.pop(idx)

        fs = collections.Counter(secret)
        fg = collections.Counter(guess)
        cows = 0
        for key in fg.keys():
            mlen = min(fg[key], fs[key])
            cows += mlen
        
        return '{}A{}B'.format(bulls, cows)


stime = time.time()
print("1A3B" == Solution().getHint("1807", "7810"))
print('elapse time: {} sec'.format(time.time() - stime))