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
        

grid = [
['0', 'E', '0', '0'],
['E', '0', 'W', 'E'],
['0', 'E', '0', '0'],
] # 3

sol = Solution()
ret = sol.bomb(grid)
print(ret)