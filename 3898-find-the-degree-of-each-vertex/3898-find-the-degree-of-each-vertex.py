class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        degree = 0
        ans = []
        n = len(matrix)
        for row in matrix:
            degree = 0 
            for x in row :
                degree += x
            ans.append(degree)
        return ans