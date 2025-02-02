class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # change str to list and add sequentially add until k
        ans = 0
        for i in s:
            num = ord(i) - 96 #'a' as 1.....'z' as 26
            while num > 0:
                ans += (num % 10)
                num //= 10
        for i in range(1,k):
            num = 0
            while ans > 0:
                num += (ans % 10)
                ans //= 10
            ans = num 
        return ans

                
             
        