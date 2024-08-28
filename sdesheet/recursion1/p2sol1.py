def rec(i,arr,f):
    if i>=len(arr):
       
       if sorted(f) not in result:
        result.append(sorted(f))
       
       return
    
    rec(i+1,arr,f+[arr[i]])
    rec(i+1,arr,f)

arr=[1,2,2]
result=[]
rec(0,arr,[])

print(result)


#or




def fun(i,ds):
            if i == len(nums):
                ds.sort()
                res.add(tuple(ds))
                return
            
            ds.append(nums[i])
            fun(i+ 1, ds)
            ds.pop()
            fun(i+ 1, ds)

nums=[1,2,3,3]           
ans = []
res = set()
fun(0, [])
for it in res:
     ans.append(list(it))
print(ans)
