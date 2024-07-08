class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            lp = 0
            rp = len(words[i]) - 1
            kuku = True
            while lp < rp:
                if words[i][lp] != words[i][rp]:
                    kuku = False
                    break
                lp += 1
                rp -= 1
            if kuku:
                return words[i]
        return ""
    


    
                
        