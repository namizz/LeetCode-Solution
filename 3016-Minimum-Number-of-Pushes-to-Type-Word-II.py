class Solution:
    def minimumPushes(self, word: str) -> int:
        hashmap = Counter(word)
        arr = []
        for i in hashmap:
            arr.append(hashmap[i])
        arr.sort()
        count = 0
        ans = 0
        for i in range(len(arr)-1,-1,-1):
            if len(arr)-1-i < 8:
                ans += arr[i]
            elif len(arr)-1-i < 16:
                ans += (arr[i]*2)
            elif len(arr) - 1 - i < 24:
                ans += (arr[i]*3)
            else:
                ans += (arr[i]*4)
        return ans

        