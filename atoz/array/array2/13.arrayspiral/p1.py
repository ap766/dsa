#OBservation

#outler layer- right , bottom ,left,top .
#Every Layer in this fashion

#The row numbers 
#We can say top most is 0 - starting row index
#THen bottom is 5 - ending row index
#left is 0 - starting column index
#right is 5 - ending column index

#Implementation

#1. We can start with the top most row and print all the elements in that row
# BY traversing a for loop from left to right to indicate the column number and for the row number we use top

#2.So now it will start from the next row 
#So we move top by 1(one down)
#Now here to indicate the colum we use right and traverse loop from top to bottom for the column

#3.Now we need to decrease right by 1 
#So now the row is indicated by bottom and column we transe from right to left

#4.Now bottom has to decreases by 1
#Now column is indicared by left and we traverse from bottom to top for printing elements of the columns


#Now left has to be moved

#5.while top<bootm and left<right

#6.COnsider edge cases for single hori line  similary for vertical line

class Solution:
    def spiralOrder(self, matrix) :
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        ans=[]

        while top<=bottom and left<=right:
        
          
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            for j in range(top,bottom+1):
               ans.append(matrix[j][right])
            right-=1

            if top<=bottom:
                values=[]
                
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])           
                bottom-=1

            if left<=right:
                values=[]
                for j in range(bottom,top-1,-1):
                    ans.append(matrix[j][left])
                left+=1
            
        return ans