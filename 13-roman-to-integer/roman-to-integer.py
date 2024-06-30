class Solution:
    def romanToInt(self, s: str) -> int:
        mydic = {"I":1, "V" : 5, "X": 10, "L":50, "C":100,"D":500,"M":1000 }
        num = 0
        i = 0
        while i < len(s):
            key = s[i]
            if i < len(s)-1:
                key2 = s[i+1]
                if mydic[key2] > mydic[key]:
                    num+=(mydic[key2]-mydic[key])
                    print(num)
                    i+=1
                else:
                    num+= mydic[key]
            else:
                num += mydic[key]
            i+=1
        return num