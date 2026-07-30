class Solution:
    def minimumPushes(self, word: str) -> int:
        hashmap = Counter(word)
        sort = sorted(hashmap.items(), key=lambda x:x[1])
        replace = 0
        ans = 0
        for _,b in sort:
            push = replace//8 + 1
            # print(push, replace)
            ans += ( push * b)
            replace += 1
        return ans

        