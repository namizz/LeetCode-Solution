class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        ans = 0
        for i in range(len(citations)):
            ans = min(citations[i], len(citations)-i)
            if citations[i] >= len(citations)-i:
                return ans
        return 0

        