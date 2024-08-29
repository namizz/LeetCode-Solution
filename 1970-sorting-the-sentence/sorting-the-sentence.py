class Solution:
    def sortSentence(self, s: str) -> str:
        # split all the word
        # store them in hash map by removing the last element
        # append on another array by order 
        #join

        words = s.split(" ")
        hash = {}
        for i in range(len(words)):
            word = words[i]
            last = len(word)-1
            hash[int(word[last])] = word[:last]
        sentence = []
        for i in range(1,len(words)+1):
            sentence.append(hash[i])
        return " ".join(sentence)


        