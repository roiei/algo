import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findDuplicateSubtrees_es(self, root: TreeNode):
        if not root:
            return []
        def dfs(root, ts):
            q = [root]
            while q:
                nq = []
                while q:
                    cur = q.pop(0)
                    if None == cur:
                        ts += None,
                        continue
                    ts += cur.val,
                    q += cur.left,
                    q += cur.right,
                q = nq
        res = {}
        freq = {}
        def trace(root):
            nonlocal res, freq
            q = [root]            
            while q:
                cur = q.pop(0)
                if None == cur:
                    continue
                ts = []
                dfs(cur, ts)
                key = '->'.join([str(t) if None != t else 'None' for t in ts])
                if key not in res:
                    res[key] = ts
                    freq[key] = 0
                freq[key] += 1
                q += cur.left,
                q += cur.right,
        
        trace(root)
        freq = [k for k,v in freq.items() if v > 1]

        out = []
        for fre in freq:
            out += res[fre],
        for o in out:
            while o and None == o[-1]:
                o.pop()
        return out

    def findDuplicateSubtrees_ref_easy(self, root):
        uniq = {}
        ans = []
        def check(node):
            if not node:
                return
            lres = check(node.left)
            rres = check(node.right)
            uid = node.val, lres, rres
            if uid not in uniq:
                uniq[uid] = 0
            uniq[uid] += 1
            if 2 == uniq[uid]:  # occurred more than 2 times
                ans.append(node)
            return uid

        check(root)
        return ans

    def findDuplicateSubtrees_ref(self, root):
        uniq = collections.defaultdict()
        uniq.default_factory = uniq.__len__  # do it when no key

        count = collections.Counter()
        print(count)

        ans = []
        def lookup(node):
            if not node:
                return
            uid = uniq[node.val, lookup(node.left), lookup(node.right)]  # create key with length
            print(node.val, uid)
            count[uid] += 1
            if count[uid] == 2:  # occurred more than 2 times
                ans.append(node)
            return uid

        lookup(root)
        return ans

    def findDuplicateSubtrees(self, root):
        freq = collections.defaultdict(int)
        uniq = {}
        ans = []
        def check(node):
            if not node:
                return
            uid = (node.val, check(node.left), check(node.right))
            freq[uid] += 1
            if 2 == freq[uid]:  # occurred more than 2 times
                ans.append(node)
            return uid

        check(root)
        return ans

    


stime = time.time()
print(Solution().findDuplicateSubtrees(deserialize('[0,0,0,0,null,0,null,0,0,0,0]')))
print('elapse time: {} sec'.format(time.time() - stime))