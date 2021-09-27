class Solution:
    def get_num_enemies(self, sy, sx, grid):
        num_enemy = 0
        width = len(grid[0])
        height = len(grid)

        y = sy
        x = sx
        while x < width and 'W' != grid[y][x]:
            if 'E' == grid[y][x]:
                num_enemy+= 1
            x+= 1

        x = sx
        while x >= 0 and 'W' != grid[y][x]:
            if 'E' == grid[y][x]:
                num_enemy+= 1
            x-= 1

        y = sy
        x = sx
        while y < height and 'W' != grid[y][x]:
            if 'E' == grid[y][x]:
                num_enemy+= 1
            y+= 1

        y = sy
        while y >= 0 and 'W' != grid[y][x]:
            if 'E' == grid[y][x]:
                num_enemy+= 1
            y-= 1

        return num_enemy
        
    def bomb(self, grid: 'List[int]') -> 'bool':
        height = len(grid)
        width = len(grid[0])

        nums = []
        for y in range(height):
            for x in range(width):
                if grid[y][x] == '0':
                    nums.append(self.get_num_enemies(y, x, grid))

        return max(nums) if nums else 0

    def maxKilledEnemies(self, grid):
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        mx = 0
        
        row_cnt = 0;
        col_cnts = [0]*cols
        
        for i in range(rows):
            for j in range(cols):
                if j == 0 or grid[i][j-1] == 'W':
                    row_cnt = 0;
                    k = j
                    while k < cols and grid[i][k] != 'W':
                        if grid[i][k] == 'E':
                            row_cnt += 1
                        k += 1

                if i == 0 or grid[i-1][j] == 'W':
                    col_cnts[j] = 0
                    k = i
                    while k < rows and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            col_cnts[j] += 1
                        k += 1

                if grid[i][j] == '0':
                    mx = max(mx, row_cnt + col_cnts[j])

        return mx
        

grid = [
['0', 'E', '0', '0'],
['E', '0', 'W', 'E'],
['0', 'E', '0', '0'],
] # 3

sol = Solution()
ret = sol.maxKilledEnemies(grid)
print(ret)