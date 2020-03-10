import time


class Solution:
    def generateMatrix(self, n: int) -> 'List[List[int]]':
        ox = oy = 0
        matrix = [[0 for i in range(n)] for i in range(n)]
        cnt = 1
        while ox < (n-ox) and oy < (n-oy):
            for x in range(ox, n-ox):
                matrix[oy][x] = cnt; cnt += 1
            for y in range(oy+1, n-oy):
                matrix[y][x] = cnt; cnt += 1
            for x in range(n-ox-2, ox-1, -1):
                matrix[y][x] = cnt; cnt += 1
            for y in range(n-oy-2, oy, -1):
                matrix[y][x] = cnt; cnt += 1
            ox += 1
            oy += 1
        return matrix


stime = time.time()
print(Solution().generateMatrix(3))
print(Solution().generateMatrix(4))
print(Solution().generateMatrix(2))
print(Solution().generateMatrix(5))
print(Solution().generateMatrix(6))
print('elapse time: {} sec'.format(time.time() - stime))