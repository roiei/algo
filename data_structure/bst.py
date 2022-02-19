


import queue
import collections


class Node:
    def __init__(self, value):
        self.root = None
        self.value = value
        pass

class Tree:
    def __init__(self):
        self.root = None
        self.num  = 0

    def __deinit__(self):
        pass

    def find(self, key):
        cur = self.root
        while None != cur:
            if cur.value < key:
                cur = cur.right
            elif cur.value > key:
                cur = cur.left
            else:
                break
        return cur if cur.value == key else None

    def pre_order(self, cur):
        print(cur.value, end = ' ')
        if cur.left != None:
            self.pre_order(cur.left)
        if cur.right != None:
            self.pre_order(cur.right)

    def in_order(self, cur):
        if cur.left != None:
            self.in_order(cur.left)
        print(cur.value, end = ' ')
        if cur.right != None:
            self.in_order(cur.right)

    def post_order(self, cur):
        if cur.left != None:
            self.post_order(cur.left)
        if cur.right != None:
            self.post_order(cur.right)
        print(cur.value, end = ' ')

    def level_order(self, cur):
        q = collections.deque([cur])

        while q:
            cur = q.popleft()
            print(cur.value, end = ' ')
            if None != cur.left:
                q.append(cur.left)
            if None != cur.right:
                q.append(cur.right)

    def traverse(self, type):
        if type == 'pre':
            self.pre_order(self.root)
        elif type == 'in':
            self.in_order(self.root)
        elif type == 'post':
            self.post_order(self.root)
        elif type == 'level':
            self.level_order(self.root)
        print()

    def insert(self, node):
        par = None
        cur = self.root
        if None == cur:
            node.right = None
            node.left  = None
            self.root = node
            return

        while cur != None:
            par = cur
            if cur.value < node.value:
                direction = 'right'
                cur = cur.right
            elif cur.value >= node.value:
                direction = 'left'
                cur = cur.left

        node.parent = par
        node.left  = None
        node.right = None
        if direction == 'right':
            par.right = node
        else:
            par.left = node
        self.num += 1

    def remove(self, key):
        '''
            1)
                  [ ] <- parent
                  /             <- if left, set cur parent's left = cur
                [ ]   <- del       if right, set cur parent's right = cur
               /   \
             [ ]   [ ]
    unlink->    \
                [ ]
                   \
                  [CUR]  <- sel as cur
                  /   \
                [a]   nil

                  [ ] <- parent
                  /
                [CUR]     parent'child = cur
               /   \'     cur's right = del's right
             [ ]   [ ]    cur's left = del's left
    unlink->    \
                [ ]       
                  \'      
                   [a]    cur's parent's right = cur's previous left
            
            2)
                [ ]  <- del
                   \
                   [ ]
                  /   
                [ ]  <- sel as cur

            3)  [ ]  <- del
              nil  nil
        '''
        direction = ''
        node = self.find(key)
        if None == node:
            return

        cur = node
        if None != cur.left:    # if left exists, go to left and go to right leaf
            cur = cur.left
            direction = 'right'
            while None != cur.right:
                cur = cur.right
        elif None != cur.right:
            cur = cur.right
            direction = 'left'
            while None != cur.left:
                cur = cur.left
        else:
            cur = node  # <-- None?

        if node != self.root:
            if node.parent.right == node:
                node.parent.right = cur
            else:
                node.parent.left = cur
        else:
            self.root = cur

        # unlink
        if None != cur:
            if direction == 'right':
                cur.parent.right = cur.left  # cur's parent's right = cur's previous left
            elif direction == 'left':
                cur.parent.left = cur.right
            cur.right = node.right
            cur.left  = node.left
        return node

    def insert_at_bottom(self):
        # where ?
        pass
    def upheap(self):
        pass


tree = Tree()

values = [45, 27, 90, 20, 31, 12, 22, 80, 74, 85, 72, 75, 84, 87, 97, 101, 86]
for val in values:
    tree.insert(Node(val))

print('pre order')
tree.traverse('pre')
print('\nin order')
tree.traverse('in')
print('\npost order')
tree.traverse('post')

print('removing 90')
tree.remove(90)
print('\npost order')
tree.traverse('post')
print('\nlevel order')
tree.traverse('level')



# a
# +---------------------
# |  |   |   |   |   |   | 
# +---------------------
"""
class Heap:
    def __init__(self):
        self.n = 0
        self.a = [0]*100

    def up_heap(self, k):
        vert = self.a[k]
        while self.a[k/2] <= vert and k > 0:
            self.a[k] = self.a[k/2]
            k /= 2
        self.a[k] = vert

    def insert(self, a, n, vert):
        self.a[++self.n] = vert
        self.up_heap(self.n)

    def down_heap(self, n, k):
        vert = self.a[k]                # k is from 1 to ...down
        while k <= n/2:                 # until internal nodes (except leaf)
            i = k*2                     # leaf has no child
            if i < n and self.a[i] < self.a[i+1]:
                i++                     # make i pointing right side child
            if vert >= self.a[i]:
                break
            self.a[k] = self.a[i]       # exchagen child -> parent
            k = i
        self.a[k] = vert

    def extract(self, n):
        vert = self.a[1]                # root (not started with 0
        self.a[1] = self.a[self.n--]    # place left to root
        down_heap(self.n, 1)            # make the root goes down
        return vert

    # 11-4.WMV
    # github
        # roiei, c.d.2.1.!!

"""