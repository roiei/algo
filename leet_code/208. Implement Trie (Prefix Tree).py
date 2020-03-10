class Letter:
    def __init__(self, letter):
        self.letter = letter
        self.child = {}
        self.eow = False

class Trie:
    def __init__(self):
        self.root = Letter('*')

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Letter(ch)
            cur = cur.child[ch]
        cur.eow = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        return True if True == cur.eow else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        return True

trie = Trie();
trie.insert("apple")
print(trie.search("apple"));  # returns true
print(trie.search("app"));    # returns false
print(trie.startsWith("app"));# returns true
trie.insert("app")
print(trie.search("app"));    # returns true