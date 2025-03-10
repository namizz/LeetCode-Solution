class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # substring should contain all vowel and k consolant 
        # set of vowel in hashmap
        # number of consolant letters in variable
        vowel = {'a','e','i','o','u'}
        hashmap = {}
        c = 0
        possiblity = 0
        lp = 0
        ans = 0
        # search until the vaild vowel are found then continue while loop until invalid
        for r in range(len(word)):
            if word[r] in vowel:
                hashmap[word[r]] = hashmap.get(word[r],0) + 1
            else:
                c += 1
            while c > k:
                possiblity = 0
                if word[lp] in vowel:
                    hashmap[word[lp]] -= 1
                    if hashmap[word[lp]] == 0:
                        hashmap.pop(word[lp])
                else:
                    c -= 1
                lp += 1
            if c == k and len(hashmap) == len(vowel):
                possiblity += 1
                ans += possiblity
        return ans
                 

        