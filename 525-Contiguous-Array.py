class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0:-1}
        a = 0
        c = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1
            else:
                c -=1
            if c in hashmap:
                a = max(a, i - hashmap[c])
            else:
                hashmap[c] = i
        return a



        