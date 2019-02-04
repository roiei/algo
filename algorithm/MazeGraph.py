import queue

class Vertex:
    def __init__(self, id, x, y):
        self.adj = []
        self.id = id
        self.x = x
        self.y = y
        self.visit = False
        self.distance = 0

    def is_exist_adj(self, v):
        for av in self.adj:
            if v.x == av.x and v.y == av.y:
                return True
        return False

    def add_adj(self, v):
        self.adj.append(v)


class MazeGraph:
    def __init__(self, limitx, limity):
        self.verts = []
        self.limitx = limitx
        self.limity = limity

    def clear(self):
        del self.verts
        self.verts = []

    def find(self, v):
        for vert in self.verts:
            if v.x == vert.x and v.y == vert.y:
                return True
        return False

    def getVert(self, x, y):
        for vert in self.verts:
            if vert.x == x and vert.y == y:
                return vert
        return None

    def add(self, v):
        if True == self.find(v):
            return False
        self.verts.append(v)

    def get_near_coord(self, x, y, limitx, limity, dir):
        nx = ny = -1
        if 'West' == dir:
            if x > 1:
                nx = x - 1
                ny = y
        elif 'East' == dir:
            if x < limitx - 1:
                nx = x + 1
                ny = y
        elif 'South' == dir:
            if y < limity - 1:
                nx = x
                ny = y + 1
        elif 'North' == dir:
            if y > 1:
                nx = x
                ny = y - 1
        return nx, ny

    def link(self, x, y):
        v = self.getVert(x, y)
        if None == v:
            print('No vertex %d, %d' %(x, y))
            return False
        for dir in ['North', 'East', 'South', 'West']:
            nx, ny = self.get_near_coord(v.x, v.y, self.limitx, self.limity, dir)
            #print('linking: {}:{},{} -> DIR {:5s} : {},{}'.format(
            #    v.id, v.x, v.y, dir, nx, ny))
            if -1 == nx or -1 == ny:
                continue    # no need to link (not exist)
            nvert = self.getVert(nx, ny)
            if None == nvert:
                continue
            if False == nvert.is_exist_adj(v):
                nvert.add_adj(v)
            if False == v.is_exist_adj(nvert):
                v.add_adj(nvert)
        return True

    def dfs(self, start_x, start_y):
        vert = self.getVert(start_x, start_y)
        traqueue = queue.Queue()
        vert.visit = True
        traqueue.put(vert)

        while not traqueue.empty():
            v = traqueue.get()
            print('{},{}'.format(v.x, v.y))
            for adv in v.adj:
                if False == adv.visit:
                    adv.visit = True
                    traqueue.put(adv)

    def mcst(self):pass

    def is_reachable(self, start_x, start_y, id):
        vert = self.getVert(start_x, start_y)
        if None == vert:
            print('No start {}, {}'.format(start_x, start_y))
        traqueue = queue.Queue()
        vert.visit = True
        traqueue.put(vert)
        reachable = False
        while not traqueue.empty():
            v = traqueue.get()
            if id == v.id:
                print('FOUND: {}:{},{}'.format(v.id, v.x, v.y))
                reachable = True
            #print('{},{}'.format(v.x, v.y))
            for adv in v.adj:
                if False == adv.visit:
                    adv.visit = True
                    traqueue.put(adv)
        return reachable

    def print_info(self):
        for v in self.verts:
            print('{}:{},{}'.format(v.id, v.x, v.y))
            for av in v.adj:
                print('\t{}:{},{}'.format(av.id, av.x, av.y))
            print()



#######################################################

mazes = [
"""#< #  #
#  #  #
#  # >#""", 
"""<   #   >""", 
"""<     >""",
"""########
#<     #
#  ##  #
#  ##  #
#     >#
########""",
"""#######
#<    #
##### #
#     #
# #####
# #   #
# # # #
#   #>#
#######"""
]

def check_reachable(startx, starty, maze_lines):
    limitx = len(maze_lines[0])
    limity = len(maze_lines)
    maze   = MazeGraph(limitx, limity)

    for y in range(limity):
        for x in range(limitx):
            if '#' == maze_lines[y][x]:
                continue
            maze.add(Vertex(maze_lines[y][x], x, y))

    for y in range(limity):
        for x in range(limitx):
            if '#' == maze_lines[y][x]:
                continue
            maze.link(x, y)

    print(maze.is_reachable(startx, starty, '>'))

def get_start_coord(maze):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if '<' == maze[y][x]:
                return x, y
    return -1, -1

def print_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            print(maze[y][x], end =' ')
        print()

for maze in mazes:
    maze_lines = maze.split('\n')
    print_maze(maze_lines)
    x, y = get_start_coord(maze_lines)
    if -1 == x or -1 == y:
        continue
    print('start coordinate', x, y, sep = ',')
    check_reachable(x, y, maze_lines)
    print()
        
