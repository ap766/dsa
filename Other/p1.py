class Solution:
    
    # Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, nums):
        v = []
        for i in range(len(nums)):
            v.append([nums[i], i])
        v.sort()
        
        swap = 0
        i = 0
        
        while i < len(nums):
            ele, pos = v[i][0], v[i][1]
            
            if i != pos:
                v[i][0], v[i][1] = v[pos][0], v[pos][1]
                v[pos][0], v[pos][1] = ele, pos
                swap += 1
            else:
                i += 1
                
        return swap

#LEARNED SOMETHING VERY IMPORTANT THAT IN A FOR LOOP OF PYTHON YOU CANT MANIPYLATE THE I