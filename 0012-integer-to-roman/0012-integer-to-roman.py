class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = {1:"I",4:"IV", 5:"V",9:"IX", 10:"X",40:"XL", 50:"L",90:"XC", 100:"C",400:"CD", 500:"D",900:"CM", 1000:"M"}
        arr = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        ans = []
        i = 0
        while num > 0:
            if num >= arr[i]:
                ans.append(hashmap[arr[i]])
                num -= arr[i]
            else:
                i += 1
        print(ans)
        return "".join(ans)

        