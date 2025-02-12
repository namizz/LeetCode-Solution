class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # their sum should be the same and make a computation
        hashmap ={}
        for i in range(len(nums)):
            temp = nums[i]
            key = 0
            while temp > 0:
                key += (temp%10)
                temp //= 10
            if key in hashmap:
                hashmap[key].append(nums[i])
            else:
                hashmap[key] = [nums[i]]
        print(hashmap)
        ans = 0
        for k,v in hashmap.items():
            j = 0
            v.sort()
            while len(v) > 1 and j < len(v)-1: 
                ans = max(ans, v[j]+v[j+1])
                j += 1

        return ans if ans else -1


        