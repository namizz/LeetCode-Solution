class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # we create a hashmap and store the first word
        # on the second iteration we check if the second letters char are in hashmap if the we store in another hashmap

        hashmap = Counter(words[0])
        common = {}
        for i in range(1,len(words)):
            for j in words[i]:
                if j in hashmap:
                    if j not in common:
                        common[j] = 1
                    elif hashmap[j] > common[j]:
                        common[j] += 1
            hashmap = common
            common = {}
        ans = []
        for k in hashmap:
            i = hashmap[k]
            while i > 0:
                ans.append(k)
                i -= 1
        return ans


        
