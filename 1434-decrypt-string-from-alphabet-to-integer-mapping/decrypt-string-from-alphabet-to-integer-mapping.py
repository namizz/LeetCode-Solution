class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s)-1
        ans =[]
        print(chr(98))
        while i > -1:
            if s[i]=='#':
                ans.append(chr(int(s[i-2:i])+96))
                i -= 3
            else:
                ans.append(chr(int(s[i])+96))
                i -= 1
        return ''.join(ans[::-1])
                
        