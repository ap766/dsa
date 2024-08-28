
def longestCommonPrefix( v) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        print(v)
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 
    
print(longestCommonPrefix(["abcd","abc","abref","abcde"]))

