class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #we sort the array
        # what we need is the max-min = 1 
        # 1,2,2,2,3,3,5,7
        # option one using hash map
        hashmap = {}
        arr = []
        ans = 0
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
                arr.append(nums[i])
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] == 1:
                ans = max(ans, hashmap[arr[i+1]] + hashmap[arr[i]])
        return ans


    
        
        
        