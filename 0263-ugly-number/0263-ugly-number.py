class Solution:
    def isUgly(self, n: int) -> bool:
        temp = n
        if temp == 0:
            return False
        while(1):
                if(temp%2 == 0):
                    temp /=2
    
                elif (temp % 3 == 0):
                    temp /= 3
                elif (temp % 5 == 0):
                    temp /= 5
                else:
                    if temp == 1:
                        return True
                    else:
                        return False
