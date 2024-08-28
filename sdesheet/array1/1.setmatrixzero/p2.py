# Marking Phase:
# Traverse the matrix and mark the rows and columns that need to be zeroed out in two separate arrays.

# Zeroing Phase:
# Traverse the matrix again and update the elements based on the markings in the arrays.


# Time Complexity:

# Marking Phase: 
# O(N×M)
# Each cell of the matrix is checked once to mark rows and columns.

# Zeroing Phase: 
# O(N×M)
# Each cell of the matrix is checked once to set zeros based on the marked rows and columns.

# Total Time Complexity: 
# O(2×(N×M))=O(N×M)



def zeroMatrix(matrix, n, m):
    row = [0] * n  # row array  ***
    col = [0] * m  # col array  ***

    # Traverse the matrix:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # mark ith index of row wih 1:
                row[i] = 1

                # mark jth index of col wih 1:
                col[j] = 1

    # Finally, mark all (i, j) as 0
    # if row[i] or col[j] is marked with 1.
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0

    return matrix


