class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # stack store in lexigraphical order when it is not monotonic remove the from stack if it' s a duplicate
        hashmap = Counter(s)
        stack = []
        set1 = set()
        for i in range(len(s)):
            if s[i] not in set1:
                while stack and stack[-1] > s[i] and hashmap[stack[-1]] > 1:
                    hashmap[stack[-1]] -= 1
                    set1.remove(stack.pop())
                
                stack.append(s[i])
                set1.add(s[i])
            else:
                hashmap[s[i]] -= 1

        return \\.join(stack)
            
        