class Solution:
    def smallestNumber(self, num: int) -> int:
        #return minimum number
        #for negative number make the number the largest
        #for postive number make the smaller number without leading 0
        digits = []
        if num < 0:
            digits = list((str(num)[1:]))
            digits.sort(reverse= True)
            return int("-"+("".join(digits)))
        else:
            i = 0
            digits = list((str(num)))
            digits.sort()
            if digits[0]=="0":
                pointer = 1
                while pointer < len(digits):
                    if digits[pointer] is not "0":
                        digits[0], digits[pointer] = digits[pointer], digits[0]
                        break
                    pointer += 1
            return int("".join(digits))
            


        