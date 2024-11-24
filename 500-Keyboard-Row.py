class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        #  change the row to set
        # by knowing the first letters row check all other letters in the letter if pass append
        ans = []
        row1 = set(\q w e r t y u i o p\.split(\ \))
        row2 = set(\a s d f g h j k l\.split(\ \))
        row3 = set(\z x c v b n m\.split(\ \))
        def checker(w, word, row):
            for i in w:
                if i not in row:
                    return False
            ans.append(word)
        for word in words:
            w = word.lower()
            if w[0] in row1:
                checker(w,word, row1)
            elif w[0] in row2:
                checker(w,word, row2)
            else:
                checker(w,word, row3)
        return ans

        