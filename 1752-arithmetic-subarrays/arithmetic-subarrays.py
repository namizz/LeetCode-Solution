class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            
            #check for arthmetic sequence
            condition = True
            if len(temp) > 1:
                rang = temp[0] - temp[1]
                for j in range(1,len(temp)-1):
                    if rang != temp[j] - temp[j+1]:
                        condition = False
                        break
            ans.append(condition)
        return ans
            
        