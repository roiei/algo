import time


# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def is_existing_node(self, onodes, val):
        for i in range(len(onodes)):
            if val == onodes[i].val:
                return True
        return False

    def get_node(self, onodes, val):
        for i in range(len(onodes)):
            if val == onodes[i].val:
                return onodes[i]
        return None

    def copy_graph(self, node):
        trav = []
        q = [node]
        onodes = []
        while q:
            cur = q.pop(0)
            if cur.val in trav:
                continue
            trav.append(cur.val)
            #print(cur.val, end=' -> ')
            if False == self.is_existing_node(onodes, cur.val):
                ncur = Node(cur.val, [])
                onodes.append(ncur)
            else:
                ncur = self.get_node(onodes, cur.val)
            for n in cur.neighbors:
                if False == self.is_existing_node(onodes, n.val):
                    new_node = Node(n.val, [])
                    new_node.neighbors.append(ncur)
                    ncur.neighbors.append(new_node)
                    onodes.append(new_node)
                if n.val not in trav:
                    q.append(n)
        return onodes

    def bfs(self, node):
        q = [node]
        visit = []
        while q:
            cur = q.pop(0)
            if cur.val in visit:
                continue
            visit.append(cur.val)
            print(cur.val, end=' -> ')
            for n in cur.neighbors:
                if n.val not in visit:
                    q.append(n)

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        onodes = self.copy_graph(node)
        #print(onodes[0].val)
        #print('onodes...')
        #self.bfs(onodes[0])
        return onodes


node1 = Node(1, [])
node2 = Node(2, [])
node3 = Node(3, [])
node4 = Node(4, [])
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

stime = time.time()
print(Solution().cloneGraph(node1))
print('elapse time: {} sec'.format(time.time() - stime))