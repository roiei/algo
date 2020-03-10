import time


def guess(num):
    if num == 1:
        return 0
    elif num < 1:
        return 1
    elif num > -1:
        return -1


class Solution(object):
    def guessNumber(self, n):
        left = 0; right = n
        while left <= right:
            mid = (right+left)//2
            res = guess(mid)
            if 0 == res:
                return mid
            elif 1 == res:
                left = mid+1
            elif -1 == res:
                right = mid-1
        return mid



stime = time.time()
print(Solution().guessNumber(1)) # bac
print('elapse time: {} sec'.format(time.time() - stime))