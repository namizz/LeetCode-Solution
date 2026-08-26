class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        right = 0
        l = 0
        ans = ""
        count = 0
        for r in range(len(s)):
            if s[r] == "1":
                count += 1
            while count > k:
                if s[l] == "1":
                    count -= 1

                l += 1
            if count == k:
                while s[l] == "0":
                    l += 1
                temp = s[l:r+1]
                if (not ans or 
                len(temp) < len(ans) or 
                (len(temp) == len(ans) and temp < ans)):
                    ans = temp
        
        
        return ans
            
            
            
            

        