import time

class Solution:
    def get_ch(self, num):
        return chr(num + ord('A'))

    def convertToTitle(self, n: int) -> str:
        out = ''
        while n > 0:
            n -= 1
            out += self.get_ch(n%26)
            n //= 26
        return out[::-1]


stime = time.time()
sol = Solution()
print(sol.convertToTitle(701)) # 'ZY'
print('elapse time: {} sec'.format(time.time() - stime))