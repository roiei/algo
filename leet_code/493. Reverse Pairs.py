import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
import bisect



class Solution1:
    def reversePairs(self, nums: [int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] > nums[j]*2:
                    cnt += 1
        return cnt


class TreeNode:
    def __init__(self, val):
        self.cnt = 1
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def search(self, node, val):
        if None == node:
            return 0
        if node.val < val:
            return node.cnt + self.search(node.right, val)
        else:
            ret = 0
            if node.val < val:
                ret = node.cnt
            return ret + self.search(node.left, val)
    
    def insert(self, root, node):
        cur = root
        exit = False
        while False == exit:
            if cur.val == node.val:
                cur.cnt += 1
                break
            if cur.val < node.val:
                if cur.right != None:
                    cur = cur.right
                else:
                    cur.right = node
                    exit = True
            else:
                cur.cnt += 1
                if cur.left != None:
                    cur = cur.left
                else:
                    cur.left = node
                    exit = True
    
    def reversePairs_bst(self, nums: [int]) -> int:
        if not nums:
            return 0
        cnt = 0
        root = TreeNode(nums.pop()*2)
        while nums:
            num = nums.pop()
            cnt += self.search(root, num)
            self.insert(root, TreeNode(num*2))
        print(cnt)
        return cnt


    def reversePairs(self, nums):
        if not nums:
            return 0
        
        res = self.merge_sort_count(nums, 0, len(nums) - 1)
        return res

    def merge_sort_count(self, nums, start, end):
        if start == end:
            return 0
        
        mid = (start + end)//2
        cnt = self.merge_sort_count(nums, start, mid)
        cnt += self.merge_sort_count(nums, mid + 1, end)

        i, j = start, mid + 1

        while i <= mid and j <= end:
            if nums[i] > nums[j]*2:
                print('nums = {}, i = {}, j = {}, add = {}'.format(nums, i, j, mid + 1 - i))
                cnt += mid + 1 - i
                j += 1
            else:
                i += 1

        nums[start:end + 1] = sorted(nums[start:end + 1])
        return cnt



stime = time.time()
#print(2 == Solution().reversePairs([1,3,2,3,1]))
#print(3 == Solution().reversePairs([2,4,1,3,5]))
#print(3 == Solution().reversePairs([2,4,3,5,1]))

print(40 == Solution().reversePairs([233, 2000000001, 234, 2000000006, 235, 2000000003, 236, 2000000007, 237, 2000000002, 2000000005, 233, 233, 233, 233, 233, 2000000004]))
print('elapse time: {} sec'.format(time.time() - stime))


