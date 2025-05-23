class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        alpha = []
        for i in range(len(s)):
            if not s[i].isdigit():
                alpha.append(i)
        # print(alpha)
        if not alpha:  # all characters are digits
            return [s]
        ans = []
        for i in range(2**(len(alpha))):
            # print(i, bin(i))
            k = i
            pos = []
            for j in range(len(alpha)):
                upto = alpha[j]
                if not j:
                    pos.extend(s[:upto])
                else:
                    frm = alpha[j-1]+1
                    pos.extend(s[frm: upto])
                #change the letter
                if k&1:
                    if s[alpha[j]].islower():
                        pos.append(s[alpha[j]].upper())
                    else:
                        pos.append(s[alpha[j]].lower())

                
                #don't change the letter
                else:
                    pos.append(s[alpha[j]])

                k >>= 1
            pos.extend(s[alpha[-1]+1:])
            # print(pos)
            ans.append("".join(pos))
        return ans

        