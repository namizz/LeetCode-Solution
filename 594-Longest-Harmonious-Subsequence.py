class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #we sort the array
        # what we need is the max-min = 1 
        # 1,2,2,2,3,3,5,7
        # option one using hash map
        hashmap = Counter(nums)
        ans = 0
        for i in hashmap:
            if (i+1) in hashmap:
                ans = max(ans, hashmap[i] + hashmap[i+1])
        return ans


    
        
        
        