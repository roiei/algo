class Solution:
    def countAndSay(self, n: int) -> str:
        tbl = {}
        tbl[1] = '1'
        tbl[2] = '11'
        cur = '11'
        for i in range(3, 30+1):
            out = ''
            idx = 0
            while len(cur) > idx:
                count = 0
                while len(cur) > idx+1:
                    if cur[idx] != cur[idx+1]:
                        break
                    count += 1
                    idx += 1
                out += str(count+1)
                out += cur[idx]
                idx += 1
            if 0 == idx:
                out = cur[idx]
            tbl[i] = out[::]
            cur = tbl[i]
        
        return tbl[n]

sol = Solution()
print(sol.countAndSay(1))