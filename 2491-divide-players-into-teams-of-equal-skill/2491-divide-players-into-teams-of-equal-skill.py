class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans = 0
        val = skill[0]+skill[-1]
        for i in range(len(skill)//2):
            if skill[i]+skill[len(skill)-i-1] != val:
                return -1
            ans += (skill[i]*skill[len(skill)-i-1])
        return ans