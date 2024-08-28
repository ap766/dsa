#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        h={}
        sum=0
        maxlen=0
        for i in range(0,len(arr)):
            sum+=arr[i]
            if sum==0:
                maxlen=i+1
            else:
                if sum in h:
                   maxlen=max(maxlen,i-h[sum])
                else:
                   h[sum]=i
           
        return maxlen