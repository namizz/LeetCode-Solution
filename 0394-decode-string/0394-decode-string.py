class Solution:
    def decodeString(self, s: str) -> str:
        arr = []
        prefix = []
        ans = []
        const = 1
        opened = 0
        i = 0
        while i < len(s):
            if not opened:
                const = 1
            temp = []
            while s[i].isdigit():
                temp.append(s[i])
                i += 1
            if temp:
                const = int("".join(temp))
            if s[i] == '[':
                prefix.append(const)
                arr.append([])
                opened += 1
            elif s[i] == ']':
                opened -= 1
                if opened:
                    x = arr.pop()*prefix.pop()
                    arr[-1].extend(x)
            else:
                if not opened:
                    arr.append([])
                    prefix.append(1)
                arr[-1].append(s[i])
            i += 1
        for i in range(len(arr)):
            ans.extend(arr[i]*prefix[i] )
        return "".join(ans)



        