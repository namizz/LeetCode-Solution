class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        #nums = [], x:int
        # return number of operation--> element to be removed from numsleft and right most element
        # if we have to hashmap with right->left prefix sum 
        # starting from the beginning of the array i-->len(nums):
        # check if there is a x-prefix sum exists in hashmap if yes add index of the prefix sum + right->left ps
        # return
        # if ps > x return -1
        hashmap = {0:0}
        ps = 0
        ans = -1
        for i in range(len(nums)-1,-1,-1):
            ps += nums[i]
            if ps not in hashmap:
                hashmap[ps] = len(nums)-i
        print(hashmap)
        ps = 0
        for i in range(len(nums)):
            if x-ps in hashmap:
                if ans == -1:
                    ans = hashmap[x-ps]+i
                ans = min(ans, hashmap[x-ps]+i)
            if x-ps < 0:
                break
            ps += nums[i]
        return ans if ans <= len(nums) else -1

            
        