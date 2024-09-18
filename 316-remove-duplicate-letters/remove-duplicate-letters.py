class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        duplicate = Counter(s)
        stack = []
        letter = set()
        for i in range(len(s)):
            if s[i] not in letter:
                while stack and stack[-1] >= s[i]:
                    if duplicate[stack[-1]] > 1:
                        letter.remove(stack[-1])
                        duplicate[stack[-1]] -= 1
                        stack.pop()
                    else:
                        break
                stack.append(s[i])
                letter.add(s[i])
            else:
                duplicate[s[i]] -= 1
        return "".join(stack)


            
        