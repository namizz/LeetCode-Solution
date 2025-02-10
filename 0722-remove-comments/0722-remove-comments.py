class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        # if you get // don't add it on array
        # iterate through the line and use flag 
        # make flag true if you get /*
        # if you get */ make the flag false
        # enter all element if flag is false and leave the if flag is true
        comment = False
        ans = []
        temp = []
        for s in source:
            if not comment:
                temp = []
            i = 0
            while i < len(s):
                if i+1 < len(s):
                    if not comment and s[i:i+2] =='//':
                        break
                    elif not comment and s[i:i+2] =='/*':
                        comment = True
                        i += 1
                    elif comment and s[i:i+2]=='*/':
                        comment = False
                        i += 1
                    else:
                        if not comment:
                            temp.append(s[i])
                else:
                    if not comment:
                        temp.append(s[i])
                i += 1
            if temp and not comment:
                ans.append("".join(temp))
        return ans
            

                
               