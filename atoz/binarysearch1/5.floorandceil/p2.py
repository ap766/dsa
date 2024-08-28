#Ceil - Same as lower bound 
#Floor - Largest number less than x

class Solution:
    # User function Template for python3
    
    # Complete this function
    def findFloor(self, arr, N, X):
        ans = -1  # Initialize ans to -1 (indicating no floor found initially)
        l = 0
        h = N - 1
        
        while l <= h:
            mid = (l + h) // 2
            
            if arr[mid] <= X:
                ans = mid  # Update ans to the current mid value
                l = mid + 1  # Move to the right half to find a larger floor
            else:
                h = mid - 1  # Move to the left half to find a smaller value
                
        return ans  # Return the found floor value or -1 if no floor exists

