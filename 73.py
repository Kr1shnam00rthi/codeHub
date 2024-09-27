class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=[]
        col=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)

        for x in row:
            y=matrix[x]
            for i in range(len(y)):
                matrix[x][i]=0
        for y in col:
            for i in range(len(matrix)):
                matrix[i][y]=0
