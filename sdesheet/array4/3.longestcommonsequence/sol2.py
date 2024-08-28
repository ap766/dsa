#Longest Consecutive Sequence
def longestsuccesiveelements(a):
    
    a.sort()
    n=len(a)

    if n==0:
        return 0
    

    lastelement=float('inf')
    longest=1
    cnt=0
    

    for i in range(n):
       
        if lastelement+1==a[i]:
            cnt+=1
  
            lastelement=a[i]
        elif lastelement!=a[i]:
            cnt=1
            lastelement=a[i]
        longest=max(cnt,longest)

    return longest
# Test the function
print(longestsuccesiveelements([2,3,4,5,6]))