class Solution:
    def simplifyPath(self, path: str) -> str:
        ops= {".",".."}
        s = path.split("/")
        stack = []
        print(s)
        for d in s:
            if d not in ops and d != "":
                stack.append(d)
            elif stack and d == "..":
                stack.pop()
        return "/"+"/".join(stack)
            

        