class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # iterate in nested loop and search if the word[i] in  word[j]
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(words[i]) <= len(words[j]) and words[i] == words[j][:len(words[i])] and words[i] == words[j][len(words[j])-len(words[i]):]:
                    count+=1
        return count