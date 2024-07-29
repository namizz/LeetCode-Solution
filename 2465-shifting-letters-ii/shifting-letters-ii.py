class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shifter = [0 for _ in range(len(s) + 1)]
        print(shifter)
        for start, end, d in shifts:
            if d == 0:
                shifter[start] -= 1
                shifter[end + 1] += 1
            else:
                shifter[start] += 1
                shifter[end + 1] -= 1
        adder = 0
        for i in range(len(s)):
            adder += shifter[i]
            c = chr(((ord(s[i]) + adder) - 97) % 26 + 97)
            s = s[:i] + c + s[i + 1:]
        return s