class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        ans = []
        for a,b in queries:
            if not a:
                ans.append(arr[b])
            else:
                ans.append(arr[b] ^ arr[a-1])
        return ans
            
        