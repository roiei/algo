
class Solution(object):
    def trap1(self, height):
        if not height:
            return 0

        height[0:0] = [0]
        rows = max(height)
        cols = len(height)

        matrix = [[0 for x in range(cols)] for y in range(rows)]
        for x in range(cols):
            for y in range(rows-1, rows-height[x]-1, -1):
                matrix[y][x] = 1
        for y in range(rows):
            print(matrix[y])

        tot_trap_cnt = 0
        for y in range(rows):
            left_blk = 0
            right_blk = 0
            trap_cnt = 0
            for x in range(cols):
                if 0 == matrix[y][x]:
                    continue
                if left_blk == 0:
                    print('lb = 0, x = ', x)
                    left_blk = x
                elif right_blk == 0:
                    right_blk = x
                    print('[{}][{}] = {}, l = {}, r = {}'.format(y, x, matrix[y][x], left_blk, right_blk))
                    trap_cnt+= right_blk - (left_blk+1)
                    print('+ = ', right_blk - left_blk)
                    left_blk = right_blk
                elif left_blk == right_blk:
                    right_blk = x
                    print('[{}][{}] = {}, l = {}, r = {}'.format(y, x, matrix[y][x], left_blk, right_blk))
                    trap_cnt+= right_blk - (left_blk+1)
                    print('+ = ', right_blk - left_blk)
                    left_blk = right_blk
            tot_trap_cnt += trap_cnt

        return tot_trap_cnt

    def trap(self, height: 'List[int]') -> int:
        if not height:
            return 0
        fill = 0
        n = len(height)
        while True:
            mcur = max(height)
            if 0 == mcur:
                break
            line = [i for i in range(n) if mcur == height[i]]
            for i in range(len(line)-1):
                fill += line[i+1] - line[i] - 1
            height = [h-1 if h == mcur else h for h in height]
        return fill

    def trap(self, height: 'List[int]') -> int:
        if not height:
            return 0
        

        left = height.pop(0)
        n = len(height)
        right = 0

        for i in range(n):
            if left > height[i]:
                right = height[i]
                if i == n - 1:
                    min(left, right)
                continue




height = [2, 0, 2] # 2

print(6 == Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
