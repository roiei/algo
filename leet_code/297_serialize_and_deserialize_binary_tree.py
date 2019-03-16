import ast
import collections


class Codec:
    def serialize(self, root):
        que, res = collections.deque([root]), []
        while que:
            node = que.popleft()
            if node:
                res.append(str(node.val))
                que.append(node.left)
                que.append(node.right)
            else:
                res.append('n')
        return ",".join(res)

    def deserialize(self, data):
        def dec(s):
            return None if s == 'n' else TreeNode(int(s))

        it = iter(data.split(","))
        que = []
        root = dec(next(it))
        if root:
            que.append(root)

        while que:
            node = que.pop(0)
            node.left = dec(next(it))
            node.right = dec(next(it))
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        self.traverse_level(root)
        return root

    def traverse_level(self, root):
        q = []
        q.append(root)
        while q:
            cur = q.pop(0)
            if None == cur:
                print('None', ' -> ', end='')
                continue
            print(cur.val, ' -> ', end='')
            q.append(cur.left)
            q.append(cur.right)