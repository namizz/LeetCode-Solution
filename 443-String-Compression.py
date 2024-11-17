from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        index = 0  
        i = 0

        while i < len(chars):
            char = chars[i]
            count = 1
            while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                count += 1
                i += 1
            chars[index] = char
            index += 1
            if count > 1:
                for digit in str(count):
                    chars[index] = digit
                    index += 1

            i += 1

        return index
