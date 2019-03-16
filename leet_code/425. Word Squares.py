
class Solution:
    def get_perms(self, words, n, depth, trace, skip, perms):
        if n == depth:
            perms.append(trace[:])
            return
        for i in range(n):
            if i in skip:
                continue
            skip.append(i)
            trace.append(words[i])
            self.get_perms(words, n, depth+1, trace, skip, perms)
            trace.pop()
            skip.pop()

    def get_combs(self, words, n, depth, r, start, trace, combs):
        if depth == r:
            combs.append(trace[:])
            return
        for i in range(start, n):
            trace.append(words[i])
            self.get_combs(words, n, depth+1, r, i+1, trace, combs)
            trace.pop()

    def check_square(self, perms, word_len):
        n = len(perms)
        square_idxs = []
        for i in range(n):
            is_square = True
            for j in range(len(perms[i])):
                for k in range(word_len):
                    if perms[i][j][k] != perms[i][k][j]:
                        is_square = False
                        break
                if False == is_square:
                    break
            if True == is_square:
                square_idxs.append(i)

        return square_idxs if square_idxs else None
        
    def get_word_squares(self, words):
        n = len(words)
        word_len = len(words[0])
        combs = []
        self.get_combs(words, n, 0, word_len, 0, [], combs)
        for i in range(len(combs)):
            perms = []
            self.get_perms(combs[i], n-1, 0, [], [], perms)
            square_idxs = self.check_square(perms, word_len)
            if None != square_idxs:
                for idx in range(len(square_idxs)):
                    print('square: ', perms[square_idxs[idx]])        


words = ["area","lead","wall","lady","ball"]

sol = Solution()
ret = sol.get_word_squares(words)
print(ret)
