class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.hashmap = defaultdict(int)
        self.nums1 = nums1
        self.nums2 = nums2
        for k in nums1:
            for v in nums2:
                self.hashmap[k+v] += 1
            

    def add(self, index: int, val: int) -> None:
        for k in self.nums1:
            self.hashmap[k+self.nums2[index]] -= 1
        self.nums2[index] += val
        for k in self.nums1:
            self.hashmap[k+self.nums2[index]] += 1
        

    def count(self, tot: int) -> int:
        return self.hashmap[tot]
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)