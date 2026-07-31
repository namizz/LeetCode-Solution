class Solution:
    def minimumPushes(self, word: str) -> int:
        letter = Counter(word)
        sh = sorted(letter.items(),key=lambda x:x[1], reverse=True)
        count = 0
        ans = 0
        for _,b in sh:
            ans += (count//8 + 1)*b
            count += 1
        return ans

        