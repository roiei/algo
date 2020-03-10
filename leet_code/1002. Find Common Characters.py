import time


class Solution:
    def commonChars2(self, A):
        n = len(A)
        common = list(A[0])
        for i in range(1, n):
            for j in range(len(common)):
                cc = common.count(common[j])
                mc = min(cc, A[i].count(common[j]))
                k = 0
                if cc > mc:
                    while k < cc - mc:
                        common[common.index(common[j])] = '@'
                        k += 1
        return [v for v in common if v != '@']

    def commonChars(self, A):
        n = len(A)
        common = list(A[0])
        for i in range(1, n):
            ncomm = []
            done = []
            for j in range(len(common)):
                if common[j] in done:
                    continue
                done.append(common[j])
                cc = common.count(common[j])
                mc = min(cc, A[i].count(common[j]))
                if mc == 0:
                    continue
                ncomm.extend([common[j] for k in range(mc)])
            common = ncomm
        return common

    def commonChars(self, A):
        
        A = [list(a) for a in A]
        comm = A[0][::]
        
        for i in range(1, len(A)):
            new_comm = []
            for j in range(len(comm)):
                if comm[j] in A[i]:
                    new_comm += comm[j],
                    A[i].pop(A[i].index(comm[j]))
            comm = new_comm
        
        return comm


stime = time.time()
print(["e","l","l"] == Solution().commonChars(["bella","label","roller"]))
print(['c', 'o'] == Solution().commonChars(["cool","lock","cook"]))
print('elapse time: {} sec'.format(time.time() - stime))