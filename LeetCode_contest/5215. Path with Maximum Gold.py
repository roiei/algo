

class Solution(object):
    def getMaximumGold(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0]*cols for _ in range(rows)]
        
        def dfs(y, x, visited, inc, mx):
            visited.add((y, x))
            mx[0] = max(mx[0], inc + grid[y][x])
            
            for oy, ox in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ny = oy + y
                nx = ox + x
                if not (0 <= ny < rows and 0 <= nx < cols) or not grid[ny][nx]:
                    continue
                if (ny, nx) in visited:
                    continue
                    
                dfs(ny, nx, visited, inc + grid[y][x], mx)
            
            visited.discard((y, x))

        mx = [0]
        for y in range(rows):
            for x in range(cols):
                if grid[y][x]:
                    dfs(y, x, set(), 0, mx)

        return mx[0]


print(24 == Solution().getMaximumGold(grid = [[0,6,0],[5,8,7],[0,9,0]]))
print(28 == Solution().getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))