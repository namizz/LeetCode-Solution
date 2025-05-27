class Solution:
    def sortSentence(self, s: str) -> str:
        arr = []
        for i in s.split():
            temp = 1
            while i[-temp].isdigit():
                temp += 1
            arr.append([i[-temp+1:], i[:-temp+1]])
        
        arr.sort()
        return " ".join([arr[i][1] for i in range(len(arr))])


        