class Solution:
    def stringSequence(self, target: str) -> List[str]:
        #the first click will be key1
        # until you get the target[i] add 1 in ascii and append that to ans(output)
        # when you get the target[i] append             /|\
        # loop end on i == len(target)                   |
        #   nested loop-----------------------------------
        #comparable= ascii of the target[i]
        # letter = comparable
        # letter += 1
        # append(arr[i]=char(letter))
        #if letter == comparable 
        #break
        ans = []
        appear = []
        for i in range(len(target)):
            comparable = ord(target[i])
            letter = ord("a")
            appear.append("a")
            ans.append("".join(appear))
            while letter != comparable:
                letter += 1
                appear[i] = chr(letter)
                ans.append("".join(appear))

        return ans
        #a,aa,ab,aba,


        