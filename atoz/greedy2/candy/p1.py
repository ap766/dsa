#OBSERVATION - NEETCODE
#Lets try out with different cases.
#1 2 3 4 5 
#5 4 3 2 1 - we notice that if we do this from beginning to end we would have to revisit and so 
#there would have to be nested loops resulting in n^2 time complexity

#SO if its a normal - non asc/non desc order we will do both - once go from left to right(we will com
# paring with left neighbour) and then right to left(we will compare with right neighbour)

class Solution:
    def candy(self, ratings) -> int:
        arr=[1]*len(ratings)
        
        for i in range(1,len(ratings)):
            if ratings[i-1]<ratings[i]:
                arr[i]=arr[i-1]+1
            
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                arr[i]=max(arr[i],arr[i+1]+1)
                
                
        return sum(arr)

#OR THE STRIVER WAY - 

#OBSERVATION
#1)Find the max of left neighbour and right neighbour

class Solution:
    def candy(self, ratings) -> int:
        left=[0]*len(ratings)
        right=[0]*len(ratings)
        n=len(ratings)
        left[0]=1
        right[n-1]=1
        
        for i in range(1,len(ratings)):
            if ratings[i-1]<ratings[i]:
                left[i]=left[i-1]+1
            else:
                left[i]=1
            
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right[i]=max(right[i],right[i+1]+1)
            else:
                right[i]=1
                
           
        sum=0
        for i in range(0,len(ratings)):
            sum+=max(left[i],right[i])
            
        return sum
    

    
#O(3N) - TC
#0(2N) - SC

#2ND WAY LETS COMPUTE ON THE FLY , LETS TAKE A CUR WHICH IS 1 AND A RIGHT WHICH IS 1