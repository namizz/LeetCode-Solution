class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            k = "".join(sorted(s))
            if k in hashmap:
                hashmap[k].append(s)
            else:
                hashmap[k] = [s]
        ans = []
        for i in hashmap:
            ans.append(hashmap[i])
        return ans