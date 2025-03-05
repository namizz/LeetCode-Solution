class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        hashmap = Counter(s)
        ans = ["1"] * (hashmap["1"]-1) + ["0"]*hashmap['0'] + ["1"]
        return "".join(ans)
        