class Solution:
    def frequencySort(self, s: str) -> str:
        f = Counter(s)
        ans = 0
        reversef = {}
        s = []
        ans = ""
        for i in f:
            if f[i] not in reversef:
                reversef[f[i]] = [i]
            else:
                reversef[f[i]].append(i)

        for i in reversef:
            s.append(i)
        s.sort(reverse = True)

        for i in s:
            for j in reversef[i]:
                ans+= j*i
        return ans


        



        