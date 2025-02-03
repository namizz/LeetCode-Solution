class Solution:
    def maskPII(self, s: str) -> str:
        # s: str s-> email or phone_number
        # return the masked info
        # if email:
        #  all letter should be lower case
        #  middle letter should be replaced with ["*"] * 5
        # if phone:
        #  don't consider {'+', -, (, ), ''} as elements
        #  (***-***-XXXX) this standard form to mask
        #````````````````````````````````````````````````````#
        # use flag 
        # for emial separate s by @, .
        # the first letter and last letter of splited before @ and lower letter else
        # for phone:
        # ignore separation and append int
        # use standard string and and append 4 int
        isEmail = False
        arr = s.split('@')
        ans = []
        if len(arr) > 1:# is email
            ans.append(arr[0][0].lower())
            ans.append("*****") 
            ans.append(arr[0][len(arr[0])-1].lower())
            ans.append("@")
            ans.extend(arr[1].lower())
        else:# is phone_number
            temp = []
            separator = {'+', '-', '(',')',' '}
            for i in range(len(s)):
                if s[i] not in separator:
                    temp.append(s[i])
            digits = len(temp)
            while digits > 10:
                if not ans:
                    ans.append('+')
                else:
                    ans.append('*')
                digits -= 1
            ans.extend(list("***-***-"))
            ans.extend(temp[-4:])
        return "".join(ans)

            
