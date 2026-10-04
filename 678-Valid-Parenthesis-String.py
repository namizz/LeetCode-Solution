class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        hig = 0
        for i in range(len(s)):
            if s[i] == '(':
                low, hig = low+1,hig+1
            elif s[i] == "*":
                low, hig = low-1, hig+1  
            else:
                low, hig = low-1,hig-1
            low = max(0,low)
            if hig < 0:
                return False
        return low == 0
                

        