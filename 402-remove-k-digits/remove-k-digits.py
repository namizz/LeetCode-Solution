class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k >= n:
            return "0"
        stack = []
        j, i = 0, 0
        while j < n:
            while stack and k > 0 and stack[-1] > num[j]:
                stack.pop()
                k -= 1
            stack.append(num[j])
            j += 1
        
        while k > 0:
            stack.pop()
            k -= 1
            
        if i < n:
            stack.extend(num[j:])
        result = "".join(stack).lstrip('0')
        return result if result else "0"
