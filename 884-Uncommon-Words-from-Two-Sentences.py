class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        #two hashmap that contain both s1 and s2 word 
        #check if the element exist both in s1>1 and s2, store , reverse
        hashmap1 = Counter(s1.split(" "))
        hashmap2 = Counter(s2.split(" "))
        ans = []
        for word in s1.split(" "):
            if hashmap1[word] == 1 and (word not in hashmap2):
                ans.append(word)
        for word in s2.split(" "):
            if hashmap2[word] == 1 and (word not in hashmap1):
                ans.append(word)

        return ans
            

        