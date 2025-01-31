class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        ans = []
        while i < len(command):
            if command[i] == "G":
                ans.append("G")
                i += 1
            elif command[i] == "(" and command[i+1] == ")":
                ans.append("o")
                i += 2
            else:
                ans.append("al")
                i += 4
        return "".join(ans)