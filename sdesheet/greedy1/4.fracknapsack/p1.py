#INTUITON
#WE NOTICE PER UNIT (GREEDILY THINK)

#1)Sort in descending cus we want max profit. based on the value per weight.
#2)And then we pick up there a chance at the last we have to take fraction.

class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w

class Solution:    
    # Define the compare method.
    def compare(self, item):
        return item.value / item.weight

    def fractionalknapsack(self, W, arr, n):
        # Use self.compare to access the compare method.
        items = sorted(arr, key=self.compare, reverse=True)
        
        curweight = 0
        maxvalue = 0
        
        for i in range(0, n):
            if (curweight + items[i].weight <= W):
                curweight += items[i].weight
                maxvalue += items[i].value
            else:
                remwt = W - curweight
                maxvalue += items[i].value * (remwt / items[i].weight)
            
                break
        return maxvalue
