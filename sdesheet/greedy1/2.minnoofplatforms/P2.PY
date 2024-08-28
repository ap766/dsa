#ANUJ

#NlogN

#INTUITION
#Interesction - IMplies that many platforms required
#Each train's arrival and departure can be considered as two separate events.
#We are interested in knowing how many trains are at the station at the same time, 
#which corresponds to needing a platform for each train.


#Just use 2 pointers and go about doing it.

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here

        
            # Sort arrival and departure arrays
            arr.sort()
            dep.sort()
            
            # Initialize variables to store the count of platforms needed and the maximum platforms needed
            count = 0
            ans = 0
            
            # Initialize pointers for arrival and departure arrays
            i, j = 0, 0
            
            # Loop through all arrival times
            while i < n:
                # If arrival time is less than or equal to the departure time
                if arr[i] <= dep[j]:
                    count += 1  # A platform is needed
                    ans = max(ans, count)  # Update the maximum platforms needed
                    i += 1
                else:
                    count -= 1  # A platform is freed
                    j += 1
            
            return ans