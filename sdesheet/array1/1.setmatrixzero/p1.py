#Identify Rows and Columns to be Zeroed:
# We need to identify which rows and columns contain a zero. However, marking them immediately can lead to incorrect results as we might alter rows and columns that haven’t been checked yet.

# Marking with Temporary Value:
# Instead of setting zeros immediately, we mark the relevant rows and columns with a temporary value (-1), which indicates that this row or column should eventually be zeroed out. This marking helps us avoid changing the matrix elements prematurely.

# Final Update:
# Once all relevant rows and columns are marked, we perform another pass over the matrix to update all marked cells to zero.

# Step 1:
# Combined Marking Complexity:
# For each zero found, marking the row and column takes 𝑂(𝑁+𝑀) time
# In the worst case, there could be O(N×M) zeros, leading to the marking phase taking O((N×M)×(N+M)) time.
                                                                                       
# Step 2: Zeroing Phase
# Traversal of the Matrix:
# We traverse the entire matrix again to convert all -1s to 0.
# This traversal takes O(N×M) time.

