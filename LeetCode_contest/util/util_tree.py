import ast


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def deserialize(data):
    if None == data:
        return None
    temp = data.replace('null', 'None')
    data = ast.literal_eval(temp)

    node = TreeNode(data[0]) if None != data[0] else None
    q = [node]
    idx = 1
    while q and idx < len(data):
        cur = q.pop(0)
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
            t += cur.val,
            if None != cur.left:
                nq += cur.left,
            if None != cur.right:
                nq += cur.right,
        q = nq
        ts += t,
    return ts
