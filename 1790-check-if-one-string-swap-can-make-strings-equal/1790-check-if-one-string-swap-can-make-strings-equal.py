class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c1 = []
        c2 = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                c1.append(s1[i])
                c2.append(s2[i])
        print(c1, c2)
        if len(c1) > 2 or len(c2) > 2 or len(c1) != len(c2) or c1[::-1] != c2:
            return False
        return True 

        