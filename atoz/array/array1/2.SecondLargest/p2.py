class Solution:
    def getSecondLargest(self, arr):
        largest = float('-inf')
        secondlargest = float('-inf')
        
        for i in range(len(arr)):
            if arr[i] > largest:
                secondlargest = largest
                largest = arr[i]
            elif arr[i] < largest and arr[i] > secondlargest:
                secondlargest = arr[i]
        
        if secondlargest == float('-inf'):
            return -1
        
        return secondlargest

# Example usage:
sol = Solution()
print(sol.getSecondLargest([1, 2, 3, 4, 5]))  # Output: 4
print(sol.getSecondLargest([5, 5, 5, 5, 5]))  # Output: -1
print(sol.getSecondLargest([2, 1]))           # Output: 1
print(sol.getSecondLargest([1]))              # Output: -1