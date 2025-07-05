class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = Counter(arr)
        ans = -1
        for i in hashmap:
            if i == hashmap[i]:
                ans = max(i, ans)
        return ans

        