class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # words1 = [], words2=[]
        # return [if "".join(word2) in words1[i]]
        # iterate throught the whole strings character check if word2 in words1?
        # method1 use hashmap
        ans = []
        hashmap = Counter()
        for word in words2:
            freq = Counter(word)
            for char, count in freq.items():
                hashmap[char] = max(hashmap[char], count)
        for word in words1:
            container = Counter(word)
            t = False
            for key in hashmap:
                if key not in container or hashmap[key] > container[key]:
                    t= False
                    break
                t = True
            if t:
                ans.append(word)




        return ans

        