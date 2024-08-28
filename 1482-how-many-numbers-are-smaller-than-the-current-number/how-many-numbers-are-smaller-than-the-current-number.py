class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s_nums = sorted(nums)
        hash ={s_nums[0]:0}
        ans = []
        for i in range(1,len(nums)):
            if s_nums[i-1] != s_nums[i]:
                hash[s_nums[i]] = i
        print(hash)
        for i in range(len(nums)):
            ans.append(hash[nums[i]])
        return ans

            
            

        