
class Solution:
    def totalFruit(self, tree: 'List[int]') -> 'int':
        if tree.count(0) + tree.count(1) == len(tree):
            return len(tree)
        if len(tree) < 1 or len(tree) > 40000:
            return 0
        if tree.count(0) == len(tree):
            return len(tree)
        lengths = []
        for i in range(len(tree)):
            length = 0
            bsk_kind = []
            for j in range(i, len(tree), 1):
                if tree[j] not in bsk_kind and len(bsk_kind) == 2:
                    break
                if tree[j] not in bsk_kind:
                    bsk_kind.append(tree[j])
                length += 1

            lengths.append(length)
        print(lengths)
        return max(lengths)

tree = [1, 2, 1]
tree = [1,2,3,2,2]
tree = [3,3,3,1,2,1,1,2,3,3,4]

print(tree.count(1))

sol = Solution()
print(sol.totalFruit(tree))

