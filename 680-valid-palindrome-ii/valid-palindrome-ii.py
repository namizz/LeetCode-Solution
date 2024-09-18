class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(lp, rp):
            while lp < rp:
                if s[lp] == s[rp]:
                    lp += 1
                    rp -= 1
                else:
                    return False
            return True
        lp = 0
        rp = len(s) - 1
        while lp < rp:
            if s[lp] == s[rp]:
                lp += 1
                rp -= 1
            else:
                return check(lp, rp - 1) or check(lp + 1, rp)
        
        
                    
        return True
                    



             

        