class Solution:
    def largestGoodInteger(self, num: str) -> str:
        z = 0
        for i in range(len(num)):
            if num[i] != 0:
                break
            z += 1
        count = 1
        ans = "0"
        for i in range(z, len(num)):
            if i > 0 and num[i-1] == num[i]:
                count += 1
            else:
                count = 1
            if count == 3 and int(ans) <= int(num[i-2:i+1]):
                ans = num[i-2:i+1]
        return ans if len(ans) > 1 else "" 
            

        