class Solution:

            
            
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        col0=1
        m=len(matrix) #no of rows
        n=len(matrix[0]) #no of columns
        for i in range(0,m):
            for j in range(0,n):
                
                if matrix[i][j]==0:
                   matrix[i][0]=0
                   
                   if j==0:
                      col0=0
                   else:
                      matrix[0][j]=0
                
        for i in range(1,m):
            for j in range(1,n):
                
               
                    if matrix[i][0]==0 or matrix[0][j]==0:
                        
                       matrix[i][j]=0
                
       
        if matrix[0][0]==0:
             for i in range(0,n):
                 matrix[0][i]=0
        if col0==0:
            for j in range(0,m):
                matrix[j][0]=0
                
                
                    
        
    
     
#Marker Placement  
# Use the first row and the first column of the matrix to mark which rows and columns should be zeroed.
# Additionally, use a separate variable col0 to keep track of whether the first column should be zeroed since the first column of the matrix will also be used for marking.

# Marking Phase:
# Traverse the matrix and for each zero found in matrix[i][j], set matrix[i][0] and matrix[0][j] to zero.
# If the zero is in the first column (j == 0), set col0 to zero.

# Zeroing Phase:
# Using the markers in the first row and column, traverse the matrix again starting from the second row and column, setting matrix[i][j] to zero if matrix[i][0] or matrix[0][j] is zero.
# Finally, if the first cell of the matrix (matrix[0][0]) is zero, zero out the first row.
# If col0 is zero, zero out the first column.


# Time Complexity:

# Initial Marking Phase: 
# O(N×M)
# Each cell of the matrix is checked once.

# Zeroing Phase: 
# O(N×M)
# Each cell of the matrix is checked once again.

# Final Adjustment Phase: 
# O(N+M)
# Each cell in the first row and first column is checked once.

# Total Time Complexity: 
# O(2×(N×M))=O(N×M)