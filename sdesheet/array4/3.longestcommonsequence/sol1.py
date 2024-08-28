#Longest consequetive sequence


def linearsearch(a,num):
    for i in range(0,len(a)):
        if a[i]==num:
            return True
    return False


def longestse(a):
    n=len(a)
    longest=1
    for i in range(n):
        x=a[i]
        cnt=1 #to keep finding the consequetive

        #to check if next one(x+1) is consequetive nd then next nd next till true, that is
        while linearsearch(a,x+1):
            x+=1
            cnt+=1

        longest=max(longest,cnt)
    return longest


a=[100,200,1,2,3,4]
ans=longestse(a)
print(ans)