class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #we sort the array
        # what we need is the max-min = 1 
        # 1,2,2,2,3,3,5,7
        # option one using hash map
        # using 3 memory start, difference, end
        nums.sort()
        start = 0
        middle = 0
        end = 0
        ans = 0
        while end < len(nums):
            if nums[start] == nums[end]:
                middle += 1
                end += 1
            elif nums[start]+1 == nums[end]:
                end += 1
            else:
                if abs(nums[start]-nums[end-1]) == 1:
                    ans = max(ans, end-start)
                    start = middle
                    middle = end
                else:
                    start = end
                    middle = end
        if nums[end-1] - nums[start] == 1:
            ans = max(ans, end-start)
        return ans
        
        