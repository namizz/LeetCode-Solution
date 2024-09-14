class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        ans = []
        i = 0
        while i < len(word) and ch != word[i]:
            stack.append(word[i])
            i += 1
        if i == len(word):
            return word
        stack.append(word[i])
        i += 1
        while stack:
            ans.append(stack.pop())
        ans.append(word[i:])
        print("".join(ans))
        return "".join(ans)
        
        