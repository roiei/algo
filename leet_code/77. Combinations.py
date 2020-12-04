

class Solution:
    cache = {}
    seq = []

    def comb(self, a, k, depth, cur_seq):
        if depth == k:
            idx = ''
            for s in cur_seq:
                idx += str(s)
            if idx not in self.cache:
                self.cache[idx] = True             
                self.seq.append(cur_seq)
            return
        if not a:
            return
        cur_seq.append(a[0])
        sub = a[1:]

        if not sub and a:
            self.comb(sub[::], k, depth+1, cur_seq[::])
        else:
            while sub:
                self.comb(sub[::], k, depth+1, cur_seq[::])
                sub.pop(0)
    
    def combine(self, n, k):
        a = [i+1 for i in range(n)]
        self.seq = []
        self.cache = {}

        for i in range(len(a)):
            cur = a[i]
            sub = a[i+1:]
            cur_seq = []
            cur_seq.append(a[i])

            if not sub and a:
                self.comb(sub[::], k, 1, cur_seq[::])
            else:
                while sub:
                    self.comb(sub[::], k, 1, cur_seq[::])
                    sub.pop(0)
        return self.seq
    

print(Solution().combine(3, 2))
