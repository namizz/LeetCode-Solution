class Solution:
    def residuePrefixes(self, s: str) -> int:
        contain = set()
        residue = 0
        for i in range(len(s)):
            if s[i] not in contain:
                contain.add(s[i])
            if len(contain) == (i+1)%3:
                residue += 1
            elif len(contain) > 3:
                break

        return residue

        