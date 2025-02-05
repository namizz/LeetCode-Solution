class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        arr = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        ans = []
        i = 0
        while num > 0:
            if num >= arr[i]:
                ans.append(hashmap[i])
                num -= arr[i]
            else:
                i += 1
        return "".join(ans)

        