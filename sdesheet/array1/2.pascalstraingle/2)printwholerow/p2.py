#we observe the number of elements is equal to the row number
#So here the row number is also telling us the number of elements in the column so we can traverse through each column this way

r=int(input())
res=1
print(res,end=" ")
for i in range(1,r):
    res=res*(r-i)
    res=res//(i)
    print(res,end=" ")

#here the time complexity is o(r)