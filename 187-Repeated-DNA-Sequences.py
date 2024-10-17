class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        hashmap = {}
        ans = []
        for i in range(len(s)-10+1):
            window = s[i:i+10]
            if window in hashmap:
                hashmap[window] += 1
            else:
                hashmap[window] = 1
            
        for i in hashmap:
            if hashmap[i] > 1:
                ans.append(i)
        return ans

        