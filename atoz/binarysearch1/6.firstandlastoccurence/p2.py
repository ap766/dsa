#1. So cus sorted we do binary search



#1. So of course to implemeent it is we consider the search space first
#2. Then since they are asking for the first occurence even when we find the element we keep trying if it occurs in the first somewhere and trim the last
#3. Similarly for the last and trim the front

class Solution:
    def searchRange(self, nums, target: int) :
        
        posstart = -1
        posend = -1
        low = 0
        high = len(nums) - 1
        
        # Find the start position
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                posstart = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        low = 0
        high = len(nums) - 1
        
        # Find the end position
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                posend = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return [posstart, posend]
        
        