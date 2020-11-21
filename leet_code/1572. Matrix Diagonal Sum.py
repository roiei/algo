
import time


class Solution:
    def diagonalSum(self, mat: [[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        tot = 0
        for i in range(m):
            tot += mat[i][i]
            tot += mat[i][m - 1 - i]

        if m%2 != 0:
            mid = m//2
            tot -= mat[mid][mid]
        return tot


stime = time.time()
print(25 == Solution().diagonalSum([[1,2,3],
                                  [4,5,6],
                                  [7,8,9]]))

print(8 == Solution().diagonalSum(
    [[1,1,1,1],
     [1,1,1,1],
     [1,1,1,1],
     [1,1,1,1]]
))

print('elapse time: {} sec'.format(time.time() - stime))
