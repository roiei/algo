import time


class Solution:

    def numDecodings(self, s: str) -> int:
        def dfs(start):
            if start in mem:
                return mem[start]

            if start == n:
                return 1
            
            if s[start] == '0':
                return 0

            ret = 0
            
            for i in range(start, min(n, start + 2)):
                part = s[start:i + 1]
                num = int(part)
                if not (0 <= num <= 26):
                    continue
                ret += dfs(i + 1)

            mem[start] = ret
            return ret
        
        n = len(s)
        mem = {}
        return dfs(0)


stime = time.time()
#print(2 == Solution().numDecodings('12')) # 2
#print(3 == Solution().numDecodings('226')) # 3
#print(1 == Solution().numDecodings('101')) # 1
#print(2 == Solution().numDecodings('611')) # 2
#print(0 == Solution().numDecodings('0')) # 0
#print(0 == Solution().numDecodings('01')) # 0
print(52488 == Solution().numDecodings('226226226226226226226226262626')) # 52488
#print(Solution().numDecodings("122878836687648315"))
#print(Solution().numDecodings("6065812287883668764831544958683283296479682877898293612168136334983851946827579555449329483852397155"))
print('elapse time: {} sec'.format(time.time() - stime))