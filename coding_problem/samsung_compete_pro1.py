

# n = 5
# m = 5
# maze = [
# ['#', '#', '#', '#', '#'],
# ['#', '.', '.', 'B', '#'],
# ['#', '.', '#', '.', '#'],
# ['#', 'R', 'O', '.', '#'],
# ['#', '#', '#', '#', '#'],
# ]
# exp = 1


# n = 7
# m = 7
# maze = [
# ['#', '#', '#', '#', '#', '#', '#'],
# ['#', '.', '.', '.', 'R', 'B', '#'],
# ['#', '.', '#', '#', '#', '#', '#'],
# ['#', '.', '.', '.', '.', '.', '#'],
# ['#', '#', '#', '#', '#', '.', '#'],
# ['#', 'O', '.', '.', '.', '.', '#'],
# ['#', '#', '#', '#', '#', '#', '#'],
# ]
# exp = 5


# n = 7
# m = 7
# maze = [
# ['#', '#', '#', '#', '#', '#', '#'], 
# ['#', '.', '.', 'R', '#', 'B', '#'], 
# ['#', '.', '#', '#', '#', '#', '#'], 
# ['#', '.', '.', '.', '.', '.', '#'], 
# ['#', '#', '#', '#', '#', '.', '#'], 
# ['#', 'O', '.', '.', '.', '.', '#'], 
# ['#', '#', '#', '#', '#', '#', '#'], 
# ]
# exp = 5


# n = 10
# m = 10
# maze = [
# ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
# ['#', 'R', '#', '.', '.', '.', '#', '#', 'B', '#'],
# ['#', '.', '.', '.', '#', '.', '#', '#', '.', '#'],
# ['#', '#', '#', '#', '#', '.', '#', '#', '.', '#'],
# ['#', '.', '.', '.', '.', '.', '.', '#', '.', '#'],
# ['#', '.', '#', '#', '#', '#', '#', '#', '.', '#'],
# ['#', '.', '#', '.', '.', '.', '.', '#', '.', '#'],
# ['#', '.', '#', '.', '#', '.', '#', '.', '.', '#'],
# ['#', '.', '.', '.', '#', '.', 'O', '#', '.', '#'],
# ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
# ]
# exp = -1


# n = 3
# m = 7
# maze = [
# ['#', '#', '#', '#', '#', '#', '#'],
# ['#', 'R', '.', 'O', '.', 'B', '#'],
# ['#', '#', '#', '#', '#', '#', '#'],
# ]
# exp = 1


# n = 10
# m = 10
# maze = [
# ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
# ['#', 'R', '#', '.', '.', '.', '#', '#', 'B', '#'], 
# ['#', '.', '.', '.', '#', '.', '#', '#', '.', '#'], 
# ['#', '#', '#', '#', '#', '.', '#', '#', '.', '#'], 
# ['#', '.', '.', '.', '.', '.', '.', '#', '.', '#'], 
# ['#', '.', '#', '#', '#', '#', '#', '#', '.', '#'], 
# ['#', '.', '#', '.', '.', '.', '.', '#', '.', '#'], 
# ['#', '.', '#', '.', '#', '#', '.', '.', '.', '#'], 
# ['#', 'O', '.', '.', '#', '.', '.', '.', '.', '#'], 
# ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
# ]
# exp = 7


# n = 3
# m = 10
# maze = [
# ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
# ['#', '.', 'O', '.', '.', '.', '.', 'R', 'B', '#'], 
# ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
# ]
# exp = -1


n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(input())


def find_ptr(maze, value):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == value:
                return y, x

ry, rx = find_ptr(maze, 'R')
by, bx = find_ptr(maze, 'B')
sy, sx = find_ptr(maze, '.')


def move(direction, ry, rx, by, bx, n, m):
    if direction == 'N':
        if ry < by:
            while ry > 1 and maze[ry-1][rx] != '#':
                ry -=1
                if maze[ry][rx] == 'O':
                    break
            while by > 1 and maze[by-1][bx] != '#' and (rx != bx or by-1 != ry):
                by -=1
                if maze[by][bx] == 'O':
                    break
        else:
            while by > 1 and maze[by-1][bx] != '#':
                by -=1
                if maze[by][bx] == 'O':
                    break
            while ry > 1 and maze[ry-1][rx] != '#' and (rx != bx or ry-1 != by):
                ry -=1
                if maze[ry][rx] == 'O':
                    break
    elif direction == 'S':
        if ry > by:
            while ry < n-1 and maze[ry+1][rx] != '#':
                ry +=1
                if maze[ry][rx] == 'O':
                    break
            while by < n-1 and maze[by+1][bx] != '#' and (rx != bx or by+1 != ry):
                by +=1
                if maze[by][bx] == 'O':
                    break
        else:
            while by < n-1 and maze[by+1][bx] != '#':
                by +=1
                if maze[by][bx] == 'O':
                    break
            while ry < n-1 and maze[ry+1][rx] != '#' and (rx != bx or ry+1 != by):
                ry +=1
                if maze[ry][rx] == 'O':
                    break
    elif direction == 'W':
        if rx < bx:
            while rx > 1 and maze[ry][rx-1] != '#':
                rx -=1
                if maze[ry][rx] == 'O':
                    break
            while bx > 1 and maze[by][bx-1] != '#' and (ry != by or bx-1 != rx):
                bx -=1
                if maze[by][bx] == 'O':
                    break
        else:
            while bx > 1 and maze[by][bx-1] != '#':
                bx -=1
                if maze[by][bx] == 'O':
                    break
            while rx > 1 and maze[ry][rx-1] != '#' and (ry != by or rx-1 != bx):
                rx -=1
                if maze[ry][rx] == 'O':
                    break
    elif direction == 'E':
        if rx > bx:
            while rx < m-1 and maze[ry][rx+1] != '#':
                rx +=1
                if maze[ry][rx] == 'O':
                    break
            while bx < m-1 and maze[by][bx+1] != '#' and (ry != by or bx+1 != rx):
                bx +=1
                if maze[by][bx] == 'O':
                    break
        else:
            while bx < m-1 and maze[by][bx+1] != '#':
                bx +=1
                if maze[by][bx] == 'O':
                    break
            while rx < m-1 and maze[ry][rx+1] != '#' and (ry != by or rx+1 != bx):
                rx +=1
                if maze[ry][rx] == 'O':
                    break
    return ry, rx, by, bx


def func2(maze, ry, rx, by, bx, direction, depth, m, n, depths):
    if depth == 10:
        return False, depth
    # print('depth = ', depth)
    # print('D = {}, FROM: ry, rx = {}, {} / by, bx = {}, {}'.format(direction, ry, rx, by, bx))
    pre_ry, pre_rx = ry, rx
    ry, rx, by, bx = move(direction, ry, rx, by, bx, n, m)
    # print('        TO : ry, rx = {}, {} / by, bx = {}, {} dir = {}'.format(ry, rx, by, bx, direction))
    # print()

    not_try_same_dir = False
    if pre_ry == ry and pre_rx == rx:
        not_try_same_dir = True
    if True == not_try_same_dir:
        return False, depth
    if maze[ry][rx] == 'O':
        #print('END')
        depths.append(depth)
        return True, depth
    elif maze[by][bx] == 'O':
        return False, depth

    sub_depths = []
    rets = []
    if not (direction == 'N' and True == not_try_same_dir):
        ret, sub_depth = func2(maze, ry, rx, by, bx, 'N', depth+1, m, n, depths)
        rets.append(ret)
        sub_depths.append(sub_depth)
    if not (direction == 'S' and True == not_try_same_dir):
        ret, sub_depth = func2(maze, ry, rx, by, bx, 'S', depth+1, m, n, depths)
        rets.append(ret)        
        sub_depths.append(sub_depth)
    if not (direction == 'W' and True == not_try_same_dir):
        ret, sub_depth = func2(maze, ry, rx, by, bx, 'W', depth+1, m, n, depths)
        rets.append(ret)
        sub_depths.append(sub_depth)
    if not (direction == 'E' and True == not_try_same_dir):
        ret, sub_depth = func2(maze, ry, rx, by, bx, 'E', depth+1, m, n, depths)
        rets.append(ret)
        sub_depths.append(sub_depth)
    return True in rets, min(sub_depths)

# print('ry, rx = {}, {}'.format(ry, rx))
# print('by, bx = {}, {}'.format(by, bx))

depth = 0
depths = []
sub_depths = []
rets = []
ret, sub_depth = func2(maze, ry, rx, by, bx, 'N', depth+1, m, n, depths)
rets.append(ret)
sub_depths.append(sub_depth)
ret, sub_depth = func2(maze, ry, rx, by, bx, 'S', depth+1, m, n, depths)
rets.append(ret)
sub_depths.append(sub_depth)
ret, sub_depth = func2(maze, ry, rx, by, bx, 'W', depth+1, m, n, depths)
rets.append(ret)
sub_depths.append(sub_depth)
ret, sub_depth = func2(maze, ry, rx, by, bx, 'E', depth+1, m, n, depths)
rets.append(ret)
sub_depths.append(sub_depth)

#print('expected = ', exp)
if True in rets:
    print(min(depths))
else:
    print(-1)



