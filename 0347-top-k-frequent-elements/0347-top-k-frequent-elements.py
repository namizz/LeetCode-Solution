class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        sorthash = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        return [key for key, _ in sorthash[:k]]
