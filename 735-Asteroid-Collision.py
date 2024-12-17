class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # asteroids = []
        #stack if stack[-1] > upcoming negative leave the negative else pop form stack until the greater is found
        # stack[-1] and nums[i] are different signs one will win
        # else stack.append
        stack = []
        for i in range(len(asteroids)):
            if stack and (stack[-1] > 0 and asteroids[i] < 0):
                while stack and stack[-1] < abs(asteroids[i]) and stack[-1] > 0:
                    stack.pop()
                if stack and stack[-1] > 0 and stack[-1] == abs(asteroids[i]):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(asteroids[i])
            else:
                stack.append(asteroids[i])
        return stack
        