class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hashmap = Counter(chars)
        ans = 0
        for i in range(len(words)):
            word = Counter(words[i])
            for k,v in word.items():
                if k not in hashmap or hashmap[k] < v:
                    break
            else:            
                ans += len(words[i])
                
        return ans


        