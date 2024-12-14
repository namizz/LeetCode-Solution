class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # s : string, 
        # store all the element in hashmap
        # iterate through elements decrease from hashamp and check if all the elements in the set are 0 hm
        # else append in set or decrease from the hashmap
        unique = set()
        hashmap = Counter(s)
        print(hashmap)
        ans = []
        ps= 0
        for i in range(len(s)):
            hashmap[s[i]] -= 1
            unique.add(s[i])
            if hashmap[s[i]] == 0:
                unique.remove(s[i])
                if not unique:
                    ans.append(i+1-ps)
                    ps += ans[-1]

        return ans
            


        