class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end = False
class Trie:

    def __init__(self):
        self.root = TrieNode()        
        

    def insert(self, word: str) -> None:
        cur = self.root
        for l in word:
            pos = ord(l)-ord('a')
            if not cur.children[pos]:
                cur.children[pos] = TrieNode()
            cur = cur.children[pos]
        cur.end = True        

    def search(self, word: str) -> bool:
        cur = self.root
        for l in word:
            pos = ord(l)-ord('a')
            if not cur.children[pos]:
                return False
            cur = cur.children[pos]
        return cur.end
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for l in prefix:
            pos = ord(l)-ord('a')
            if not cur.children[pos]:
                return False
            cur = cur.children[pos]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)