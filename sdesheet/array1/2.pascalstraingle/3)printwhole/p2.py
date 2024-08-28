

class Solution:
    def generate(self, numRows: int):
        
        def calc(r): 
            ans=[1]
            res=1
            for i in range(1,r):
                res=res*(r-i)
                res=res//(i)
                ans.append(res)
            return ans
        res=[]
        for i in range(1,numRows+1):
         ans=calc(i)
         res.append(ans)
        return res
        
                










#Complexity: O(n2), where n = number of rows(given).
