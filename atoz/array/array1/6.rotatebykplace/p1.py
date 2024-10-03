#First why the ascending order wont work has been shown for right rotation we have to go from behind 
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
      
        k = k % n  # Handle cases where k > n
        if n == 1 or k == 0:
            return
        
        temp = nums[-k:]  # Store the last k elements
      
        # Shift elements forward by k positions
        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]
        
        # Place the stored k elements at the beginning
        nums[:k] = temp
