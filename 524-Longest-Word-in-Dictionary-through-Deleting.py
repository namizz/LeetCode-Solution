class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        #["ale","apple","monkey","plea"]
        ans = ""
        #aabcelpp , aelpp, ans="ale", j,k= 0,0
        for word in dictionary: 
            j = 0   
            k = 0
            while j < len(word) and k < len(s):
                if len(word[j:]) > len(s[k:]):
                    break
                if word[j] == s[k]:
                    j += 1
                k += 1
                if j == len(word):
                    if len(word) > len(ans):
                        ans = word
                    elif len(word) == len(ans):
                        ans = min(ans, word)
                    else:
                        break
        return ans


                
                

        