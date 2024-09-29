#We satrt with Window size of 1 
#2 pointers l and r l represents left most side of the window and r represents rightmost side of the window
#Initially sum as 0 
#Expand using r 
#Shrink using l

#INTUION

#Use a example like [2,5,1,7,10]
#So we can start with a window size of 1 and keep on increasing the size of the window till sum is less than k.
#And then if we notice that it exceeds the sum we can shrink from the left 
#And at every step basically we are calcuting thr largest size

l=0
r=0
sum=0
maxlen=0
arr=eval(input())
n=len(arr)
k=int(input())
while r<n:
    sum+=arr[r]

    while sum>k:
        sum-=arr[l]
        l+=1

    if sum<=k:
        maxlen=max(maxlen,r-l+1)
   
    r+=1

#Time complexity is not o(n^2)
#overall o(2n)
