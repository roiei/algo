import time

class Solution:
    mem = {}
    def bfs(self, y, x, n, m):
        if y == n-1 and x == m-1:
            return 1
        idx = '{}:{}'.format(y, x)
        if idx in self.mem:
            return self.mem[idx]
        num = 0
        if y < n:
            num += self.bfs(y+1, x, n, m)
        if x < m:
            num += self.bfs(y, x+1, n, m)
        if idx not in self.mem:
            self.mem[idx] = num
        return num

    def uniquePaths(self, m: int, n: int) -> int:        rows = len(board)
        cols = len(board[0])
        n = len(word)
        
        def dfs(board, y, x, word, pos, trace, res):
            ch = board[y][x]
            if ch == None or ch != word[pos]:
                return False
            
            board[y][x] = None
            trace += ch,
            
            if pos == n-1:
                return True
            
            for oy, ox in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                oy += y
                ox += x
                if not (0 <= oy < rows and 0 <= ox < cols):
                    continue
                if True == dfs(board, oy, ox, word, pos + 1, trace, res):
                    return True
            
            trace.pop()
            board[y][x] = ch
            return False
        
        trie = Trie()
        trie.insert(word)
        
        res = []
        for y in range(rows):
            for x in range(cols):
                if True == dfs(board, y, x, list(word), 0, [], res):
                    return True
        return False
        self.mem = {}
        return self.bfs(0, 0, n, m)


    def uniquePaths_es(self, m: int, n: int) -> int:
        def bfs(y, x, n, m):
            if y == n-1 and x == m-1:
                return 1
            num = 0
            if y < n:
                num += bfs(y+1, x, n, m)
            if x < m:
                num += bfs(y, x+1, n, m)
            return num
        return bfs(0, 0, n, m)


stime = time.time()
sol = Solution()
print(sol.uniquePaths(3, 2))
print(sol.uniquePaths_es(3, 2))
# print(sol.uniquePaths(23, 12))
# print(sol.uniquePaths_es(23, 12))
print('elapse time: {} sec'.format(time.time() - stime))