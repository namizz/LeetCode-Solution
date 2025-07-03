class Solution:
    def kthCharacter(self, k: int) -> str:
        s = ["a"]
        while len(s) < k:
            for i in range(len(s)):
                c = chr(ord(s[i])+1)
                if c > "z":
                    c = "a"
                s.append(c)
        
        return s[k-1]


        