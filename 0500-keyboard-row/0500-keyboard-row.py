class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = {'i', 'o', 'r', 'q', 'y', 't', 'p', 'u', 'e', 'w'}
        second = {'h', 's', 'k', 'a', 'l', 'f', 'g', 'j', 'd'}
        thrid = {'n', 'x', 'z', 'm', 'c', 'v', 'b'}
        ans = []
        def oneline(w, contain,ans):
            for l in w:
                if l.lower() not in contain:
                    return
            ans.append(w)

        for word in words:
            if word[0].lower() in first:
                oneline(word, first, ans)
            elif word[0].lower() in second:
                oneline(word, second, ans)
            else:
                oneline(word, thrid, ans)
        
        return ans
        