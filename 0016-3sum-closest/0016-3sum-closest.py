class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # -4, -1, 1, 2
        #  |   |  |
        # brute force solution

        """
    4 6 2 3 8  target = 10

    closest = abs(curr_sum - target)
    2 4 7 12 16
    i        j



        """

        # let's say 2 is right and go for the two  closest
        nums.sort()
        min_diff = float(inf)
        ans = 0
        for i in range(len(nums)):
            rp = len(nums)-1
            lp = i+1
            while lp < rp:
                temp = nums[i] + nums[lp] + nums[rp]
                if temp > target:
                    rp -= 1
                elif temp < target:
                    lp += 1
                else:
                    return temp
                if min_diff > abs(temp-target):
                    ans = temp
                    min_diff = abs(temp-target)
                
        return ans



