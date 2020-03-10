
# need optimization


class Solution:
    def get_order(self, matrix, N, y, x, dir):
        if 0 == matrix[y][x] or 2 == matrix[y][x]:
            return 0
        matrix[y][x] = 2
        yl_order = yr_order = xl_order = xr_order = 0
        if ('OMNI' == dir or 'TOP' == dir) and (y > 0 and matrix[y-1][x] == 1):
            yl_order = self.get_order(matrix, N, y-1, x, 'TOP')
        if ('OMNI' == dir or 'DOWN' == dir) and (y < N-1 and matrix[y+1][x] == 1):
            yr_order = self.get_order(matrix, N, y+1, x, 'DOWN')
        if ('OMNI' == dir or 'LEFT' == dir) and (x > 0 and matrix[y][x-1] == 1):
            xl_order = self.get_order(matrix, N, y, x-1, 'LEFT')
        if ('OMNI' == dir or 'RIGHT' == dir) and (x < N-1 and matrix[y][x+1] == 1):
            xr_order = self.get_order(matrix, N, y, x+1, 'RIGHT')
        if 'TOP' == dir:
            y_order = 1 + yl_order
            return y_order
        elif 'DOWN' == dir:
            y_order = 1 + yr_order
            return y_order
        else:
            y_order = 1 + min(yl_order, yr_order)
        if 'LEFT' == dir:
            x_order = 1 + xl_order
            return x_order
        elif 'RIGHT' == dir:
            x_order = 1 + xr_order
            return x_order
        else:
            x_order = 1 + min(xl_order, xr_order)
        
        if 'OMNI' == dir:
            return min(y_order, x_order)
        return max(y_order, x_order)

    def orderOfLargestPlusSign(self, N: int, mines) -> int:
        matrix = [[1 for i in range(N)] for j in range(N)]
        for mine in mines:
            matrix[mine[0]][mine[1]] = 0
        degrees = []
        for y in range(N):
            for x in range(N):
                if 1 == matrix[y][x]:
                    degrees.append(self.get_order(copy.deepcopy(matrix), N, y, x, 'OMNI'))
        if degrees:
            return max(degrees)
        return 0