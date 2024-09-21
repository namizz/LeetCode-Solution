class Solution:
    def similarPairs(self, words: List[str]) -> int:
        d = Counter()
        count = 0
        for c in words:
            word = "".join(sorted(set(c)))
            count += d[word]
            d[word]+= 1
        return count


            

        
        