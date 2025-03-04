class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # we need to make the array sorted
        # if the array is element are sorted pass
        # else try to replace it with it's summation
        # start from back
        # check if it is largest and continue to next
        # if not nums[i] <= nums[i+1] 
        # we decrease nums[i-1] form nums[i](// without loop) mark an checkpoint---->loop
        # [7,2,2,3,3,3]
        ans = 0
        _max = float(inf)
        for i in range(len(nums)-2,-1,-1):
            _max = min(nums[i+1], _max)
            if nums[i] > _max:
                q = nums[i]//_max
                r = nums[i]% _max
                if r:
                    ans += 1
                    _max = min(nums[i]//(q+1), _max)
                _max = min(nums[i]//q, _max)
                ans += (q-1)
        return ans
        