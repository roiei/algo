
import time

class Solution:
    mem = {}
    def get_path_cost(self, grid, n, m, y, x, trace):
        if y == n-1 and x == m-1:
            trace.append(grid[y][x])
            s = sum(trace)
            trace.pop()
            return s
        idx = '{}:{}'.format(y, x)
        if idx in self.mem and self.mem[idx] <= sum(trace) + grid[y][x]:
            return self.mem[idx]
        trace.append(grid[y][x])
        cost = []
        if y < n-1:
            c = self.get_path_cost(grid, n, m, y+1, x, trace)
            cost.append(c)
        if x < m-1:
            cost.append(self.get_path_cost(grid, n, m, y, x+1, trace))
        trace.pop()
        self.mem[idx] = min(cost)
        return self.mem[idx]

    def minPathSum_es(self, grid: 'List[List[int]]') -> int:
        self.mem = {}
        return self.get_path_cost(grid, len(grid), len(grid[0]), 0, 0, [])

    def minPathSum(self, grid: 'List[List[int]]') -> int:
        n, m = len(grid), len(grid[0])
        for y in range(n):
            for x in range(m):
                if y == 0 and x == 0:
                    continue
                elif y == 0:
                    grid[y][x] += grid[y][x-1]
                elif x == 0:
                    grid[y][x] += grid[y-1][x]
                else:
                    grid[y][x] = min(grid[y-1][x], grid[y][x-1])+grid[y][x]
        return grid[y][x]

matrix = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

matrix = [
    [1,2],
    [5,6],
    [1,1]
]

matrix = [
[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]

stime = time.time()
sol = Solution()
print(sol.minPathSum(matrix))   # 7
print('elapse time: {} sec'.format(time.time() - stime))
