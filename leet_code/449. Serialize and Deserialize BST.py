import ast
import collections


class Codec:
    def serialize(self, root):
        if not root:
            return None
        trace = []
        q = [root]
        while q:
            cur = q.pop(0)
            if None != cur:
                trace.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            else:
                trace.append(None)

        while None == trace[-1]:
            trace.pop(-1)

        str_trace = ''.join(str(trace))
        ret = str_trace.replace('None', 'null')
        return ret

    def deserialize(self, data):
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

