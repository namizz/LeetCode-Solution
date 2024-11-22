class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #hashmap that store the number and there indices
        #when duplicate are found compare there difference with k if equal return true, 
        #if greter store current indice else continue
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                if i-hashmap[nums[i]] <= k:
                    return True
                else:
                    hashmap[nums[i]] = i
        return False

        