class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #sort strings in alphabetical order
        # iterate throught both strings 
        # find if magazine is formed from ransomNote
        word = Counter(magazine)
        for i in ransomNote:
            if i in word:
                word[i] -= 1
                if word[i] < 0:
                    return False
            else:
                return False
        return True
        