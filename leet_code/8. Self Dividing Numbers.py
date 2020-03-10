import time

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> 'List[int]':
        res = []
        for num in range(left, right+1):
            snum = str(num)
            is_sdn = True
            for i in range(len(snum)):
                if '0' == snum[i] or 0 != num%int(snum[i]):
                    is_sdn = False
                    break
            if True == is_sdn:
                res.append(num)
        return res

stime = time.time()
sol = Solution()

print(sol.selfDividingNumbers(1, 22)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
print('elapse time: {} sec'.format(time.time() - stime))