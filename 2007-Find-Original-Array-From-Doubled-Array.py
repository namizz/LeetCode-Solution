class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        hashmap = Counter(changed)
        changed.sort()
        ans = []
        for i in range(len(changed)):
            if changed[i]* 2 in hashmap and hashmap[changed[i]] > 0:
                hashmap[changed[i]*2] -= 1
                if hashmap[changed[i]] > 0 and hashmap[changed[i]*2] >= 0:
                    ans.append(changed[i])
                    hashmap[changed[i]] -= 1
                
        return ans if len(ans) == len(changed)/2 else []