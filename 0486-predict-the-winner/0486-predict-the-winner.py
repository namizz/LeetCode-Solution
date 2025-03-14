class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def recursion(l,r):
            if l == r:
                return nums[l]
            return max(nums[l]-recursion(l+1,r), nums[r]-recursion(l,r-1))
        return recursion(0,len(nums)-1) >= 0
        