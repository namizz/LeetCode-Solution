class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.hashmap = defaultdict(int)
        self.nums1 = nums1
        self.nums2 = nums2
        for k in nums2:
            self.hashmap[k] += 1
            

    def add(self, index: int, val: int) -> None:
        self.hashmap[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.hashmap[self.nums2[index]] += 1
        

    def count(self, tot: int) -> int:
        ans = 0
        for k in self.nums1:
            if tot-k in self.hashmap:
                ans+= self.hashmap[tot-k]
        return ans

        return self.hashmap[tot]
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)