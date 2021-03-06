
class Solution:
    def generate(self, numRows: int) -> 'List[List[int]]':
        if 0 == numRows:
            return []

        outs = [[1]]
        
        for i in range(1, numRows):
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
        return outs

    def generate(self, numRows: int) -> List[List[int]]:
        if 0 == numRows:
            return []

        line = [1]
        lines = [line]
        
        for _ in range(numRows - 1):
            new = []
            new += line[0],
            
            for i in range(len(line) - 1):
                new += line[i] + line[i + 1],
            
            new += line[-1],
            line = new
            lines += line,
        
        return lines