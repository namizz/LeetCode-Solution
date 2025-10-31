class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()        

    def addWord(self, word: str) -> None:
        cur = self.root
        for l in word:
            if l not in cur.children:
                cur.children[l] = Node()
            cur = cur.children[l]
        cur.end = True    
        

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i == len(word):
                return node.end
            c = word[i]
            if c == ".":
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                    return False
            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c],i+1)

        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)