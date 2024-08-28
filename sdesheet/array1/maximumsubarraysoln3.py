def maxSubarraySum(arr,n):
    maxi=-10**6-1
    sum=0
    for i in range(n):
            
            
            sum += arr[i]
            print(sum)
            
            if sum > maxi:
                maxi = sum

            # If sum < 0: discard the sum calculated
            if sum < 0:
                sum = 0

    if maxi<0:
         maxi=0

    return maxi


arr=[18,-6,-6,-5,7,10,16,-6,-2,0] 
n=len(arr)
print(maxSubarraySum(arr, n))

