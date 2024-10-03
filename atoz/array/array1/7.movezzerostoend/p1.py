class Solution:
    def moveZeroes(self, a: List[int]) -> None:
            n=len(a)
            
            # Temporary array
            temp = []

            # Copy non-zero elements from original to temp array
            for i in range(n):
                if a[i] != 0:
                    temp.append(a[i])

            # Number of non-zero elements
            nz = len(temp)

            # Copy elements from temp to fill first nz fields of original array
            for i in range(nz):
                a[i] = temp[i]

            # Fill the rest of the cells with 0
            for i in range(nz, n):
                a[i] = 0

            return a

