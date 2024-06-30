class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            x_s = str (x)
            x_str = list(x_s)
            left = 0
            right = len(x_str)-1
            while left < right:
                x_str[left],x_str[right]= x_str[right],x_str[left]
                left+=1
                right-=1
            y_n = ''.join(x_str)
            y = int(y_n)
            return (y == x and x >= 0)
        