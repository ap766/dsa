# Intuition: By observation, we see that the first column of the original matrix is the reverse of the first row of the rotated matrix, so that’s why we transpose the matrix and then reverse each row, and since we are making changes in the matrix itself space complexity gets reduced to O(1).

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(0,len(matrix)):
            for j in range(0,i): #the i here is very important - it would skip diagonal and only one corner elements selected

             
                
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

          
        for i in range(0,len(matrix)):
            matrix[i].reverse()

        print(matrix)
            
s=Solution()
matrix=[[1,2,3],[4,5,6],[7,8,9]]
s.rotate(matrix)



# Time Complexity: O(N^2)
# Space Complexity: O(1)
