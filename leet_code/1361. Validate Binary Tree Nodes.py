
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def validateBinaryTreeNodes2(self, n: int, leftChild: [int], rightChild: [int]) -> bool:

        def dfs(used, node, left, right):
            #print('used = {}, node = {}, left = {}, right = {}'.format(used, node, left, right))
            if node in used:
                print(node, used)
                return False

            used.add(node)

            if not left and not right:
                return True

            ll = lr = True

            if left[0] != -1:
                ll = dfs(used, left[0], left[1:], right[1:])

            if right[0] != -1:
                lr = dfs(used, right[0], left[2:], right[2:])

            return ll and lr


        used = set()
        ret = dfs(used, 0, leftChild, rightChild)
        if False == ret:
            return False
        print(ret, len(used), n)
        return ret and len(used) == n


    def validateBinaryTreeNodes(self, n: int, leftChild: [int], rightChild: [int]) -> bool:

        used = {0}

        for l, r in zip(leftChild, rightChild):
            if l != -1:
                if l in used:
                    return False
                used.add(l)

            if r != -1:
                if r in used:
                    return False
                used.add(r)

        return len(used) == n

        
        
            
stime = time.time()
print(True == Solution().validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]))
print(False == Solution().validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]))
print(False == Solution().validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1]))
print(False == Solution().validateBinaryTreeNodes(n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]))
print(True == Solution().validateBinaryTreeNodes(5, [1,-1,3,4,-1], [-1,2,-1,-1,-1]))
print(True == Solution().validateBinaryTreeNodes(4, [1,-1,3,-1], [2,-1,-1,-1]))
print(False == Solution().validateBinaryTreeNodes(4, [1,-1,3,-1], [2,3,-1,-1]))
print('elapse time: {} sec'.format(time.time() - stime))