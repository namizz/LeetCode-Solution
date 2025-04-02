class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # (nums[i] - nums[j]) * nums[k]
        # | dec | inc |
        # | dec | dec|
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] < nums[j]:
                        break
                    ans = max((nums[i]-nums[j])*nums[k], ans)
        return ans

        