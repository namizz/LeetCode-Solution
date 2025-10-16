class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]%value] = hashmap.get(nums[i] % value,0) + 1
        
        
        ans = 0
        while ans%value in hashmap and hashmap[ans%value] > 0:
         
            hashmap[ans%value] -= 1
            ans += 1
          
        return ans
        
        