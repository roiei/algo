class Solution:
    possible_cnt = 0

    def get_possible_positions(self, coords):
        possible_x = []
        possible_y = []
        possible = []
        for i in range(len(coords)):
            if coords[i][0] not in possible_x:
                possible_x.append(coords[i][0])
            if coords[i][1] not in possible_y:
                possible_y.append(coords[i][1])

        for i in range(len(possible_x)):
            possible.append([possible_x[i], -1])
        for i in range(len(possible_y)):
            possible.append([-1, possible_y[i]])
        return possible

    def is_possible(self, coords, trace):
        mark = [False for i in range(len(coords))]
        n = len(trace)
        for i in range(n):
            for j in range(len(coords)):
                if trace[i][0] == coords[j][0]:
                    mark[j] = True
                elif trace[i][1] == coords[j][1]:
                    mark[j] = True

        return True if False not in mark else False

    def get_combination(self, coords, possible, depth, r, start, trace, n):
        if depth == r:
            ret = self.is_possible(coords, trace)
            self.possible_cnt += 1
            return ret

        res = []
        for i in range(start, n):
            trace.append(possible[i])
            ret = self.get_combination(coords, possible, depth+1, r, i+1, trace, n)
            res.append(ret)
            trace.pop()

        return True if True in res else False

    def check_area(self, coords, r):
        possible = self.get_possible_positions(coords)
        n = len(possible)
        ret = self.get_combination(coords, possible, 0, r, 0, [], n)
        return ret


coords = [[1, 7],
[0, 0],
[1, 2],
[2, 0],
[1, 4],
[3, 4]]

# tc = int(input())
# coords = []
# for i in range(tc):
#     coords.append(list(map(int, input().split())))

sol = Solution()
print(sol.check_area(coords, 3))