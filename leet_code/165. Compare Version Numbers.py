import time


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        lv1 = len(v1)
        lv2 = len(v2)
        ml = min(lv1, lv2)
        res = 0
        cnt = 0
        for i in range(ml):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
            cnt += 1

        if lv1 == lv2:
            return 0
        elif lv1 > lv2:
            for j in range(cnt, lv1):
                print(j, v1[j])
                if v1[j] > 0:
                    return 1
            return 0
        elif lv1 < lv2:
            for j in range(cnt, lv2):
                if v2[j] > 0:
                    return -1
            return 0

    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        lv1 = len(v1)
        lv2 = len(v2)
        lmax = max(lv1, lv2)

        def pad(nums, pad):
            while pad:
                nums += 0,
                pad -= 1

        if lv1 < lv2:
            pad(v1, lv2 - lv1)
        else:
            pad(v2, lv1 - lv2)

        for i in range(lmax):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0


stime = time.time()
print(-1 == Solution().compareVersion('0.1', '1.1')) # -1
print(1 == Solution().compareVersion('1.0.1', '1')) # 1
print(-1 == Solution().compareVersion('7.5.2.4', '7.5.3')) # -1
print(0 == Solution().compareVersion('1.01', '1.001')) # 0
print(0 == Solution().compareVersion('1.0', '1.0.0')) # 0
print(0 == Solution().compareVersion('1.0', '1')) # 0
print(1 == Solution().compareVersion('1.0.1', '1')) # 1
#print(Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(1)).val) # ?
print('elapse time: {} sec'.format(time.time() - stime))