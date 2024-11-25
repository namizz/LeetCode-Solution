class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # apple packs that contained apples
        # we need to redistibute to capacity packs
        # return the minimum number of boxes(packs) to be selected
        # we are gonna have the number of apples
        # sort the capacity and replace the capacity packs with apples
        # when all apples are contained return the number packs
        total = 0
        ans = 0
        for i in apple:
            total += i
        capacity.sort()
        for i in range(len(capacity)-1, -1,-1):
            ans += 1
            total -= capacity[i]
            if total <= 0:
                break
        return ans
            
        