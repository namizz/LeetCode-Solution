class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]
        w = "".join(sorted(words[0]))
        for i in range(1,len(words)):
            prev = w
            w = "".join(sorted(words[i]))
            if prev != w:
                ans.append(words[i])
        return ans
        