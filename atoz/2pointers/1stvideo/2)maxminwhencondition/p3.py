#o(n) soln
#[2,5,1,10,10]
 
#Shrinking doessnt matter cus we just need need the length
#no need to make maxlen of 3 go back to 2 , its fine


l=0
r=0
sum=0
maxlen=0
arr=eval(input())
n=len(arr)
k=int(input())
while r<n:
    sum+=arr[r]

    if sum>k:
        sum-=arr[l]
        l+=1

    if sum<=k:
        maxlen=max(maxlen,r-l+1)
   
    r+=1

