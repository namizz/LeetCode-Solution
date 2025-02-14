class Solution:
    def validPalindrome(self, s: str) -> bool:
        # use two pointer and one gurentee flag
        
        lp, rp = 0, len(s)-1
        def check_left(lp, rp):
            while lp < rp:
                if s[lp] == s[rp]:
                    lp += 1
                    rp -= 1
                else:
                    return False
            return True

        while lp <= rp:
            if s[lp] == s[rp]:
                lp += 1
                rp -= 1
            else:
                return check_left(lp, rp-1) or check_left(lp+1, rp)
        return True
        