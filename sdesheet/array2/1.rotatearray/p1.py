class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        rotatedmatrix=[[0 for _ in range(n)] for _ in range(n)]
        for i in range(0,n):
            for j in range(0,n):
                rotatedmatrix[j][n-i-1]=matrix[i][j]
                
        return rotatedmatrix
            
# Approach: Take another dummy matrix of n*n, and then take the first row of the matrix and put it in the last column of the dummy matrix, take the second row of the matrix, and put it in the second last column of the matrix and so.