class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        hashmap = {}
        o = 0
        for i in range(len(nums)):
            if nums[i] == x:
                o += 1
                hashmap[o] = i
        ans = []
        for i in queries:
            if i in hashmap:
                ans.append(hashmap[i])
            else:
                ans.append(-1)

        return ans


        