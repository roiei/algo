
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        i = inorder.index(preorder[0])
        
        node = TreeNode(preorder[0])
        node.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        node.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return node

            
stime = time.time()
print(tree_is_same(deserialize('[3,9,20,null,null,15,7]'), Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])))
print('elapse time: {} sec'.format(time.time() - stime))