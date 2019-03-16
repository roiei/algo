class Solution(object):
    def make(self, cur, depth, n, res):
        if depth == n:
            res.extend(cur[:])
            return
        ncur = []
        length = len(cur) + 1
        for i in range(length):
            if i == 0:
                ncur.append(cur[0])
            elif i == length-1:
                ncur.append(cur[-1])
            else:
                ncur.append(cur[i-1] + cur[i])
        self.make(ncur, depth+1, n, res)

    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        cur = [1, 1]
        depth = 1
        res = []
        self.make(cur, depth, rowIndex, res)
        return res

sol = Solution()
ret = sol.getRow(3)
print(ret)

ret = sol.getRow(4)
print(ret)