class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [digit for digit in str(num)]
        r_digits = sorted(digits, reverse = True)
        for i in range(len(digits)):
            if digits[i] != r_digits[i]:
                for j in range(len(digits)-1,i,-1):
                    if digits[j] == r_digits[i]:
                        digits[i], digits[j] = digits[j], digits[i]
                        break
                break

        return int(''.join(digits))


        