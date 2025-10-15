class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        hashmap = {}
        dp = {}
        for i in range(len(arr)):
            if arr[i] not in hashmap:
                hashmap[arr[i]] = [i]
            else:
                hashmap[arr[i]].append(i) 
        def find(i,k):
            _min = float(inf)
            if k in hashmap:
                for index in hashmap[k]:
                    if index > i:
                        _min = min(_min, index)
            return _min


        def rec(k,i):
            if (k,i) in dp:
                return dp[(k,i)]
            if k not in hashmap:
                return 0
            a = find(i,k+difference)# k should be right of the number we are at
            b = 0
            if a != float(inf):
                b = rec(k+difference, a)
            dp[(k,i)] = 1+b
            
            return 1+b
        ans = 0
        for i in range(len(arr)):
            ans = max(ans,rec(arr[i],i))
            # print(i, ans, dp)
        return ans
