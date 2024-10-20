class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = {}
        word = s.split(" ")
        if len(word) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in hashmap:
                if hashmap[pattern[i]] != word[i]:
                    return False
            else:
                hashmap[pattern[i]] = word[i]
        value = set()
        for i in hashmap:
            if hashmap[i] in value:
                return False
            value.add(hashmap[i])

        return True
            
        