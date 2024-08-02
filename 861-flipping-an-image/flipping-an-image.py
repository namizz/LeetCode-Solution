class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            left = 0
            right = len(image[0])-1
            while left <= right:
                image[i][left], image[i][right] = image[i][right], image[i][left]
                if image[i][left] and image[i][right]:
                    image[i][left], image[i][right] = 0, 0
                elif image[i][left] and not image[i][right]:
                    image[i][left], image[i][right] = 0, 1
                elif not image[i][left] and image[i][right]:
                    image[i][left], image[i][right] = 1, 0
                else:
                    image[i][left], image[i][right] = 1, 1
                left += 1
                right -= 1
        return image


        