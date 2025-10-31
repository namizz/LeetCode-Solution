class Node:
    def __init__(self):
        self.child = [None] *26
        self.c = 0
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        curr = self.root
        for c in word:
            pos = ord(c)-ord('a')
            if not curr.child[pos]:
                curr.child[pos] = Node()
            curr.child[pos].c += 1
            curr = curr.child[pos]
    def count(self,s):
        curr = self.root
        ans = 0
        for c in s:
            pos = ord(c)-ord('a')
            ans += curr.child[pos].c
            curr = curr.child[pos]
        return ans
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for i in range(len(words)):
            trie.insert(words[i])
            
        scores = [0]*len(words)
        for i in range(len(words)):
            scores[i] = trie.count(words[i])
        return scores
        