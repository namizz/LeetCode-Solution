class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        # o(n * m)
        # o(1)
        # {
        # 1: 0, 2: 1, 4:2, 6:3
        # }
        # store on hashmap
        # do operation
        # replace the hashmap value with new value
        # return nums 
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for a, b in operations:
            index = hashmap[a]
            nums[index] = b
            del hashmap[a]
            hashmap[b] = index
        return nums 

        