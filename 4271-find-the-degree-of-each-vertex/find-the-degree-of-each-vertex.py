class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans=[0]*len(matrix)
        for i in range(len(matrix)):
            deg=0
            for j in range(len(matrix)):
                deg+=matrix[i][j]
                ans[i]=deg
        return ans