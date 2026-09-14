class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        horizontal = []
        for row in image:
            row = row[::-1]
            horizontal.append(row)
        print(horizontal)
        n = len(horizontal)
        for i in range(n):
            for j in range(n):
                if horizontal[i][j] == 1:
                    horizontal[i][j] = 0

                elif horizontal[i][j] == 0:
                    horizontal[i][j] = 1
        return horizontal