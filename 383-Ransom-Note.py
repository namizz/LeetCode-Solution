class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #sort strings in alphabetical order
        # iterate throught both strings 
        # find if magazine is formed from ransomNote
        word1 = sorted(magazine)
        word2 = sorted(ransomNote)
        w1,w2 = 0,0
        while w1 < len(word1) and w2 < len(word2):
            if word2[w2] == word1[w1]:
                w1 += 1
                w2 += 1
            else:
                w1 += 1
        return True if w2 >= len(word2) else False 
        