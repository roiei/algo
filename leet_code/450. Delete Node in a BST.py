import time
from util_list import *
from util_tree import *


class Solution:
    def find(self, root, key: int):
        par = cur = root
        while None != cur:
            if cur.val > key:
                par = cur
                cur = cur.left
            elif cur.val < key:
                par = cur
                cur = cur.right
            else:
                break
        return cur, par

    def trav_in(self, root):
        q = [root]
        while q:
            cur = q.pop(0)
            print(cur.val, end=', ')
            if None != cur.left:
                q.append(cur.left)
            if None != cur.right:
                q.append(cur.right)

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        dnode, dpar = self.find(root, key)
        if None == dnode:
            return root
        if None == dnode.left and None == dnode.right:
            if dnode == dpar:
                return None
            if dpar.left == dnode:
                dpar.left = None
            else:
                dpar.right = None
            return root
        dir = ''
        par = dnode
        if None != dnode.left:
            cur = dnode.left
            while None != cur.right:
                par = cur
                cur = cur.right
            if cur != dnode.left:
                if cur != par:
                    par.right = cur.left
                cur.left = dnode.left
            cur.right = dnode.right
            dir = 'left'
        elif None != dnode.right:
            cur = dnode.right
            while None != cur.left:
                par = cur
                cur = cur.left
            if cur != dnode.right:
                if cur != par:
                    par.left = cur.right
                cur.right = dnode.right
            cur.left = dnode.left
            dir = 'right'

        if dnode != dpar:
            if dpar.left == dnode:
                dpar.left = cur
            elif dpar.right == dnode:
                dpar.right = cur
        else:
            if 'left' == dir:
                cur.right = dnode.right
            else:
                cur.left = dnode.left
            root = cur
        return root

    def deleteNode(self, root, key):

        def dfs(node, parent):
            if not node:
                return None

            if node.val == key:
                if not node.left or not node.right:
                    node = node.left or node.right
                    return node
                elif node.left and node.right:
                    cur_node = node.left
                    while cur_node.right:
                        cur_node = cur_node.right
                    cur_node.right = node.right
                    return node.left
            elif node.val < key:
                node.right = dfs(node.right, node)
            elif node.val > key:
                node.left = dfs(node.left, node)
            return node
        
        return dfs(root, None)



stime = time.time()
#print(Solution().deleteNode(deserialize('[5,3,6,2,4,null,7]'), 3))
print(Solution().deleteNode(deserialize('[0]'), 0))
print('elapse time: {} sec'.format(time.time() - stime))