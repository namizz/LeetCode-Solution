class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # loop up to n-k start from k 
        # we need hashmap which has a function of counter
        # window in imagination with one variable that store the sum of the window
        # ans variable

        #consider the del hash map is o(n) process
        hashmap = Counter(nums[:k])
        store = sum(nums[:k])
        if len(hashmap) == k:
            ans = store
        else:
            ans = 0
        
        for i in range(len(nums)-k):
            #delete the previous and remove it from hashmap if it's value is 0 delete from hashmap
            store -= nums[i]
            hashmap[nums[i]] -= 1
            if hashmap[nums[i]] == 0:
                hashmap.pop(nums[i])
            #add the upcoming add to hash map
            store += nums[i+k]
            if nums[i+k] in hashmap:
                hashmap[nums[i+k]] += 1
            else:
                hashmap[nums[i+k]] = 1


            #if len(hashmap) < k: don't modify ans
            if len(hashmap) == k:
                ans = max(ans, store)
            print("ans", ans)
        return ans

        