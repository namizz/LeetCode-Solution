class Solution:
    def isHappy(self, n: int) -> bool:
        set1 = set()
        while n > 1:
            num = str(n)
            n = 0
            for i in num:
                n += (int(i)**2)
            if n in set1:
                break
            set1.add(n)
        return True if n == 1 else False

        
        