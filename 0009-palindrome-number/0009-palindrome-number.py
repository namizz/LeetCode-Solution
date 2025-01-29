class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        c_r = x
        rev = 0
        while c_r > 0:
            rev *= 10
            rev += c_r%10
            c_r//=10
        return x == rev


    
        
            
        