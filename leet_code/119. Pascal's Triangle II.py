

class Solution(object):
    def getRow(self, rowIndex: int) -> List[int]:
        outs = [[1]]
        
        for i in range(1, rowIndex + 1):
            out = []
            n = len(outs[-1]) + 1
            
            for j in range(n):
                if 0 == j:
                    out += outs[-1][0],
                elif n - 1 == j:
                    out += outs[-1][-1],
                else:
                    out += outs[-1][j-1] + outs[-1][j],
            outs += out,
        return outs[-1]


sol = Solution()
ret = sol.getRow(3)
print(ret)

ret = sol.getRow(4)
print(ret)