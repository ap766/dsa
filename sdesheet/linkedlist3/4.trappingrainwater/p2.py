class Solution:
    def trap(self, arr) -> int:
            n = len(arr)
            prefix = [0] * n
            suffix = [0] * n
            prefix[0] = arr[0]
            for i in range(1, n):
                prefix[i] = max(prefix[i - 1], arr[i])
            suffix[n - 1] = arr[n - 1]
            for i in range(n - 2, -1, -1):
                suffix[i] = max(suffix[i + 1], arr[i])
            waterTrapped = 0
            for i in range(n):
                waterTrapped += min(prefix[i], suffix[i]) - arr[i]
            return waterTrapped
    
    