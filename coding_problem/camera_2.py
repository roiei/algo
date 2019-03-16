class Solution:
    def get_cam_coord(self, area, starty, startx):
        for y in range(len(area)):
            for x in range(len(area[0])):
                if area[y][x] != 0 and area[y][x] != 6:
                    return y, x
        return -1, -1

    def fill(self, area, sy, sx, fill_type):
        if '1L' == fill_type:
            x = sx-1
            while x > 0:
                area[sy][x] = '#'
                x -= 1
        elif '1R' == fill_type:
            pass
        elif '1U' == fill_type:
            pass
        elif '1D' == fill_type:
            pass
        elif '2LR' == fill_type:
            pass
        elif '2UD' == fill_type:
            pass
        elif '3UR' == fill_type:
            pass
        elif '3RD' == fill_type:
            pass
        elif '3DL' == fill_type:
            pass
        elif '3LU' == fill_type:
            pass
        elif '4LUR' == fill_type:
            pass
        elif '4LDR' == fill_type:
            pass
        elif '5LRUD' == fill_type:
            pass

    def check_area(self, area, starty, startx, fill_type):
        y, x = self.get_cam_coord(area, starty, startx)
        if -1 == y:
            print('end fill')
            return True

        self.fill(area, y, x, fill_type)

        if 1 == area[y][x]:
            fill_types = ['1L', '1R', '1U', '1D']
            for i in range(len(fill_types)):
                self.check_area(area, y, x, fill_types[i])
        elif 2 == area[y][x]:
            fill_types = ['2LR', '2UD']
            for i in range(len(fill_types)):
                self.check_area(area, y, x, fill_types[i])
        elif 3 == area[y][x]:
            fill_types = ['3UR', '3RD', '3DL', '3LU']
            for i in range(len(fill_types)):
                self.check_area(area, y, x, fill_types[i])
        elif 4 == area[y][x]:
            fill_types = ['4LUR', '3LDR']
            for i in range(len(fill_types)):
                self.check_area(area, y, x, fill_types[i])
        elif 5 == area[y][x]:
            fill_types = ['5LRUD']
            for i in range(len(fill_types)):
                self.check_area(area, y, x, fill_types[i])
        return False    # no Ture means not filled


area = [
['0', '0', '2', '0', '3'],
['0', '6', '0', '0', '0'],
['0', '0', '6', '6', '0'],
['0', '0', '0', '0', '0'],
]

# tc = int(input())
# coords = []
# for i in range(tc):
#     coords.append(list(map(int, input().split())))

sol = Solution()
print(sol.check_area(coords, 3))