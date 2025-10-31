class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:

    def __init__(self):
        self.root = TrieNode()        
        

    def insert(self, word: str) -> None:
        cur = self.root
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode()
            cur = cur.children[l]
        cur.end = True        

    def search(self, word: str) -> bool:
        cur = self.root
        for l in word:
            if l not in cur.children:
                return False
            cur = cur.children[l]
        return cur.end
        

    def startsWith(self, word: str) -> str:
        cur = self.root
        prefix = []
        for l in word:
            if l not in cur.children:
                return ""  
            cur = cur.children[l]
            prefix.append(l)
            if cur.end:  
                return "".join(prefix)
        return ""  

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        ans = sentence.split(" ")
        for k,w in enumerate(ans):
            ll = trie.startsWith(w)
            if ll:
                ans[k] = ll
        return " ".join(ans)
        