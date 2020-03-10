

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        def dfs(node, trace):
            while None != node:
                trace.append(node.val)
                if None != node.child:
                    dfs(node.child, trace)
                node = node.next

        trace = []
        dfs(head, trace)
        n = len(trace)
        node = head = Node(trace[0], None, None, None)
        for i in range(1, n):
            node.next = Node(trace[i], node, None, None)
            node = node.next
        return head

    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        def trace(node):
            cur = node
            res = []
            while cur != None:
                res += cur.val,
                if cur.child != None:
                    res += trace(cur.child)
                cur = cur.next
            return res
        
        t = trace(head)
        
        pre = cur = head = Node(t.pop(0), None, None, None)
        while t:
            cur.next = Node(t.pop(0), cur, None, None)
            cur = cur.next
        cur.next = None
            
        return head

