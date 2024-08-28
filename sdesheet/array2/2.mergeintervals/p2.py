
#INUTION - Intuition: Since we have sorted the intervals, the intervals which will be merging are bound to be adjacent. We kept on merging simultaneously as we were traversing through the array and when the element was non-overlapping we simply inserted the element in our answer list.
#And also the image that we have a for loop

class Solution:
    def merge(self, intervals):
        
        ans=[]
        intervals.sort()
        
        for i in range(0,len(intervals)):
            if not ans or ans[-1][1]<intervals[i][0] :
                ans.append(intervals[i])
            else:
                ans[-1][1]=max(ans[-1][1],intervals[i][1])
                
        return ans
    
# Time Complexity: O(N*logN) + O(N), where N = the size of the given array.
# Reason: Sorting the given array takes  O(N*logN) time complexity. Now, after that, we are just using a single loop that runs for N times. So, the time complexity will be O(N).

# Space Complexity: O(N), as we are using an answer list to store the merged intervals. Except for the answer array, we are not using any extra space.