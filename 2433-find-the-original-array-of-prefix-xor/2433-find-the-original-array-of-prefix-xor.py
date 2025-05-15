class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        for i in range(1,len(pref)):
            ans.append(pref[i-1]^pref[i])
        return ans


        