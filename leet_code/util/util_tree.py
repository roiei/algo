import ast
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        self_val = None if not self else self.val
        other_val = None if not other else other.val
        return self_val == other_val


    def deserialize(seq):
        if not seq:
            return None
    
        seq = ast.literal_eval(seq.replace('null', 'None'))
        root = TreeNode(seq[0])
        q = collections.deque([root])
        idx = 1
    
        while q and idx < len(seq):
            node = q.pop(0)
            node.left = TreeNode(seq[idx]) if seq[idx] else None
            idx += 1
    
            if node.left:
                q.append(node.left)
    
            if idx < len(seq):
                node.right = TreeNode(seq[idx]) if seq[idx] else None
                idx += 1
    
                if node.right:
                    q.append(node.right)
    
        return root


def deserialize(data):
    if None == data:
        return None

    temp = data.replace('null', 'None')
    data = ast.literal_eval(temp)

    node = TreeNode(data[0]) if None != data[0] else None
    q = collections.deque([node])
    idx = 1

    while q and idx < len(data):
        cur = q.popleft()
        cur.left = TreeNode(data[idx]) if data[idx] != None else None
        idx+= 1
        if cur.left:
            q.append(cur.left)
        if idx < len(data):
            cur.right = TreeNode(data[idx]) if data[idx] != None else None
            idx+= 1
            if cur.right:
                q.append(cur.right)
    return node


def traverse_level(node):
    ts = []
    q = [node]
    while q:
        nq = []
        t = []
        while q:
            cur = q.pop(0)
            if not cur:
                continue
            t += cur.val,
            if None != cur.left:
                nq += cur.left,
            if None != cur.right:
                nq += cur.right,
        q = nq
        ts += t,
    return ts


def tree_is_same(node1, node2):
    def dfs(node1, node2):
        if not node1 and not node2:
            return True

        if (not node1 and node2) or (node1 and not node2):
            return False

        if node1.val != node2.val:
            return False

        return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

    return dfs(node1, node2)
