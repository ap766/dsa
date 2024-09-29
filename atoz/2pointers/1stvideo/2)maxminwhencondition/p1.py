#So sum<=k largest string


arr=eval(input())
k=int(input())
n=len(arr)
maxlen=0
for i in range(0,n):
    sum=0
    for j in range(i,n):
        sum+=arr[j]
        if sum<=k:
            maxlen=max(maxlen,j-i+1)
        elif sum>k:
            break
