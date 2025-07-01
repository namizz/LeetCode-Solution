class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        ans = []
        for i in range(1,k):
            if nums[i-1]+1 == nums[i]:
                r += 1
            else:
                l = r = i
        for i in range(k,len(nums)):
            print(r,l)
            if r-l+1 >= k:
                ans.append(nums[r])
            else:
                ans.append(-1)
            if nums[i-1]+1 == nums[i]:
                r += 1
            else:
                l = r = i
        ans.append(nums[-1] if r-l+1 >= k else -1) 
        return ans
            
                

        