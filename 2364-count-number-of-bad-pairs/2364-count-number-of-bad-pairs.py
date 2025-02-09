class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # nums = []
        # return number of bad pairs
        # bad pairs are i < j and j-i != nums[j]-nums[i]
        # max_bad pairs = (len(nums)-1)!
        # nums[j]-j != nums[i]-i
        # get how many nums are nums[j]-j == nums[i]-j
        # the add in their frequency and subtract from permutation(total result pair that can be made)
        hashmap = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            count += hashmap[nums[i]-i]
            hashmap[nums[i]-i] += 1
        ans = 0
        for i in range(1,len(nums)):
            ans += i
        return ans -count
        