import time


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.eow = False
        self.child = {}

class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.child:
                cur.child[letter] = TrieNode(letter)
            cur = cur.child[letter]
        cur.eow = True
    
    def search(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.child:
                return False
            cur = cur.child[letter]
        return False

class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        
        def dfs(board, y, x, word, i, n, visit):
            if i == n:
                return True
            if i == n-1 and board[y][x] == word[i]:
                return True
            if board[y][x] != word[i]:
                return False

            for oy, ox in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if not (0 <= y + oy < rows and 0 <= x + ox < cols):
                    continue
                if visit[y+oy][x+ox] == True:
                    continue
                visit[y+oy][x+ox] = True
                if True == dfs(board, y+oy, x+ox, word, i+1, n, visit):
                    return True
                visit[y+oy][x+ox] = False
            return False
        
        rows = len(board)
        cols = len(board[0])
        visit = [[False]*cols for _ in range(rows)]

        for y in range(rows):
            for x in range(cols):
                visit[y][x] = True
                if True == dfs(board, y, x, word, 0, len(word), visit):
                    return True
                visit[y][x] = False
        return False


    # with visit -> 80~85%
    def exist(self, board: [[str]], word: str) -> bool:
        
        def dfs(board, y, x, word, i, n, visit, node):
            if i == n:
                return True
            if i == n-1 and board[y][x] in node.child:
                return True
            
            if board[y][x] not in node.child:
                return False

            for oy, ox in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if not (0 <= y + oy < rows and 0 <= x + ox < cols):
                    continue
                if visit[y+oy][x+ox] == True:
                    continue
                visit[y+oy][x+ox] = True
                if True == dfs(board, y+oy, x+ox, word, i+1, n, visit, node.child[board[y][x]]):
                    return True
                visit[y+oy][x+ox] = False
            return False
        
        rows = len(board)
        cols = len(board[0])
        visit = [[False]*cols for _ in range(rows)]
        
        trie = Trie()
        trie.insert(word)

        for y in range(rows):
            for x in range(cols):
                visit[y][x] = True
                if True == dfs(board, y, x, word, 0, len(word), visit, trie.root):
                    return True
                visit[y][x] = False
        return False

    # without visit -> 65 ~ 70%
    def exist(self, board: [[str]], word: str) -> bool:
        
        def dfs(board, y, x, i, n, node):
            if board[y][x] == None:
                return False
            if board[y][x] not in node.child:
                return False
            
            if i == n-1 and board[y][x] in node.child:
                return True
            
            letter = board[y][x]
            board[y][x] = None

            for oy, ox in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if not (0 <= y + oy < rows and 0 <= x + ox < cols):
                    continue
                if True == dfs(board, y+oy, x+ox, i+1, n, node.child[letter]):
                    board[y][x] = letter
                    return True
            board[y][x] = letter
            return False
        
        rows = len(board)
        cols = len(board[0])
        
        trie = Trie()
        trie.insert(word)

        for y in range(rows):
            for x in range(cols):
                if True == dfs(board, y, x, 0, len(word), trie.root):
                    return True
        return False


board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
#words = ["oath","pea","eat","rain"]
word = 'oath'

stime = time.time()
#print(Solution().exist(board, word)) # [[1,5],[6,9]]
#print(Solution().exist([["a"]], "a"))
print(Solution().exist([["a","a"]], "aaa"))
print('elapse time: {} sec'.format(time.time() - stime))

