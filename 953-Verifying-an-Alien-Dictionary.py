class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #hashmap to find the lexiogrphical order of the letters
        # two pointers to compare the two alternatives
        letter = {}
        for i in range(len(order)):
            letter[order[i]] = i
        for i in range(len(words)-1):
            for j in range(min(len(words[i]),len(words[i+1]))):
                if (letter[words[i][j]] or 0) > (letter[words[i+1][j]] or 0):
                    return False
                elif (letter[words[i][j]] or 0) < (letter[words[i+1][j]] or 0):
                    break
                if j == min(len(words[i]),len(words[i+1]))-1 and len(words[i]) > len(words[i+1]):
                    return False
                    
        return True

        