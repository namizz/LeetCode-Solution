class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
         # uniquness of the number
         # if yes add on current ans
         # if not store the max ans 
         # remove the store number from left until the current number becomes unique
         # remove the numbers left until we get the number the same as current number
         l = 0
         ans = 0
         container = set()
         curr_ans = 0
         for i in range(len(nums)):
            if nums[i] in container:
                ans = max(ans, curr_ans)
                while nums[i] in container:
                    container.remove(nums[l])
                    curr_ans -= nums[l]
                    l += 1

            curr_ans += nums[i]
            container.add(nums[i])
         return max(ans, curr_ans)




        