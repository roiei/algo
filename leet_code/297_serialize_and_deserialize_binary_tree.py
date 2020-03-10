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



    def serialize(self, root):
        if not root:
            return ''

        def dfs(node):
            q, t = [node], []
            while q:
                node = q.pop(0)
                if not node:
                    t += None,
                else:
                    t += node.val,
                    q += node.left,
                    q += node.right,
            return t
        
        t = dfs(root)
        while t and t[-1] == None:
            t.pop()
            
        return str(t).replace('None', 'null').replace(' ', '')

    
    def deserialize(self, data):
        if '' == data:
            return None
    
        data = data[1:len(data)-1].split(',')
        vals = [data[i] for i in range(len(data))]
        
        root = TreeNode(vals.pop(0))
        q = [root]
        while q:
            node = q.pop(0)
            if vals:
                node.left = TreeNode(vals.pop(0))
                q += node.left,
            if vals:
                node.right = TreeNode(vals.pop(0))
                q += node.right,
        
        return root

