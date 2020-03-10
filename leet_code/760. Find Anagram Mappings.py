import time

class Solution(object):
    def findAnagramMappings(self, a, b):
        adict = {}
        for i in range(len(b)):
            if b[i] not in adict:
                adict[b[i]] = [i]
            else:
                adict[b[i]].append(i)
        out = []
        for i in range(len(a)):
            if a[i] in adict:
                if not adict[a[i]]:
                    return []
                out.append(adict[a[i]].pop())
        return out

# A = [12, 28, 46, 32, 50]
# B = [50, 12, 32, 46, 28]
A = [1, 2, 1, 2, 3]
B = [2, 3, 1, 2, 1]
stime = time.time()
print(Solution().findAnagramMappings(A, B))
print('elapse time: {} sec'.format(time.time() - stime))