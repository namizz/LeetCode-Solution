class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xr = 0
        for val in derived:
            xr ^= val
        return xr == 0