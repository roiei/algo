

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.idx = 0
        self.trace = []
        if not root:
            self.n = 0
            return
        self.in_order(root, self.trace)
        self.n = len(self.trace)

    def in_order(self, cur, trace):
        if None != cur.left:
            self.in_order(cur.left, trace)
        trace.append(cur.val)
        if None != cur.right:
            self.in_order(cur.right, trace)

    def next(self):
        ret = -1
        if self.idx < self.n:
            ret = self.trace[self.idx]
            self.idx+= 1
        return ret

    def hasNext(self):
        if self.idx == self.n:
            return False
        return True


root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

iterator = BSTIterator(root);
print(iterator.next())    # return 3
print(iterator.next())    # return 7
print(iterator.hasNext()) # return true
print(iterator.next())    # return 9
print(iterator.hasNext()) # return true
print(iterator.next())    # return 15
print(iterator.hasNext()) # return true
print(iterator.next())    # return 20
print(iterator.hasNext()) # return false

