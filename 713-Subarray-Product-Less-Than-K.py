class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #nums = [] k:int
        #number of subarray where their product is > k
        #method 1: brute force
        #loop the whole array
        #nested loop
        #counter =+ 1 if prefix_product < k  else break
        # method2: store the prefix product with their index in hashmap
        # ans:int--->store the number of subarrays
        # prefix_product : int---> running product check if < k: add hashmap value on ans
        # else: running product/i < k add hashmap[running product] - i
        ans = 0
        running = 1
        lp = 0
        for i in range(len(nums)):
            running *= nums[i]
            if running < k:
                ans += (i+1-lp)
            else:
                while running >= k and lp <= i:
                    running /= nums[lp]
                    lp += 1
                ans += (i+1-lp)
        return ans
                


        