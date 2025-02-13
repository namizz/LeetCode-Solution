class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # one hashmap and set
        # one contain all and the set contain non dup
        # when we pop from the first we check if could be separated
        hashmap = Counter(s)
        contain = set()
        ans = []
        prev_sum = 0
        for i in range(len(s)):
            hashmap[s[i]] -= 1
            contain.add(s[i])
            if hashmap[s[i]] <= 0:
                hashmap.pop(s[i])
                contain.remove(s[i])
                if not contain:
                    ans.append(i+1-prev_sum)
                    prev_sum = (i+1)
        return ans
        

        

        