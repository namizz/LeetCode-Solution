class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        pref = 0
        ans = 0
        for i in range(len(nums)):
            pref += nums[i]
            temp = (pref-k)%k
            if temp in hashmap:
                ans += hashmap[temp] 
            hashmap[temp] = hashmap.get(temp,0) + 1
        return ans

        