class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = ""
        i = 0
        while i < len(s):
            store = 0
            j = i%k
            while j < k:
                store += (ord(s[i])-97)
                j += 1
                i += 1
            result += chr((store%26) + 97)
        return result
                
        