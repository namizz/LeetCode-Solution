class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        nums:[], goal:int
        return nums of subarray = 2
        method 1(brute force)
        check from 1-n of array in dynamic sliding window
        then check from 2-n sum in dynamic sliding window
        method 2(prefix sum)
        [1,0,1,0,1] let's store the previous ps and check if there is prefix sum = goal
        [1,0,1,0,1] in hashmap
        {0:1, 1:2, 2:2}
        [0,0,0,0,0]
        [0,0,0,0,0]
        {0:5,
        1+2+3+4+5

        """
        ps = 0
        hashmap = {0:1}
        ans = 0
        for num in nums:
            ps += num
            if ps-goal in hashmap:
                ans += hashmap[ps-goal]
            if ps not in hashmap:
                hashmap[ps] = 1
            else:
                hashmap[ps] += 1
        return ans
                
                

        