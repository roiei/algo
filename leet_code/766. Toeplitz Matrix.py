import time


class Solution:
    def isToeplitzMatrix(self, matrix: 'List[List[int]]') -> bool:
        if not matrix:
            return False
        n = len(matrix)
        m = len(matrix[0])
        for y in range(n-1):            
            for x in range(m-1):
                if matrix[y][x] != matrix[y+1][x+1]:
                    return  False
        return True


matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]

matrix = [
  [1,2],
  [2,2]
]

matrix = [
[11, 74, 0,  93],
[40, 11, 74, 7]]


stime = time.time()
sol = Solution()
print(sol.isToeplitzMatrix(matrix))
print('elapse time: {} sec'.format(time.time() - stime))