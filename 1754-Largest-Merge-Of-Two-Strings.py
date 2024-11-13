class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        w1,w2= 0,0
     
        merge = []
        while (w1 < len(word1) and w2 < len(word2)):
            if word1[w1:] > word2[w2:] :
                merge.append(word1[w1])
                w1 += 1

            else:
                merge.append(word2[w2])
                w2 += 1

        if word1[w1:] != []:
            merge.extend(word1[w1:])
        if word2[w2:] != []:
            merge.extend(word2[w2:])

        print(merge)
        return "".join(merge)

        