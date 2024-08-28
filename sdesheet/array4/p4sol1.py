#Equal to Zero
def solve(a):
    n=len(a)
    maxx=float('-inf')
    for i in range(0,n):
        sum=0
        for j in range(i,n):
            sum+=a[j]
            if sum==0:
               maxx=max(maxx,j-i+1)

    
    return maxx
            
a=[37,4]
print(solve(a))