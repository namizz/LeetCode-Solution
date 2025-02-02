class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 99 --> 100
        i = len(digits)-1
        while digits[i] == 9 and i > 0:
            digits[i] = 0
            i -= 1
        if digits[i] == 9:
            digits[i] = 1
            digits.append(0)
        else:
            digits[i] += 1
        return digits
        