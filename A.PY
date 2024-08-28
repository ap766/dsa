class Solution:
    
    # Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, nums):
        v = []
        for i in range(len(nums)):
            v.append([nums[i], i])
        v.sort()
        
        swap = 0
        print(v)

        for i in range(len(v)):
            ele, pos = v[i][0], v[i][1]
            print(ele,end=" ")
            print(pos)
            print(".......")
            
            print("i",i,end=" ")
            print("pos",pos)

            print(",,,,,,,,,,")
            if i != pos:
                
                v[i][0], v[i][1] = v[pos][0], v[pos][1]
                v[pos][0], v[pos][1] = ele, pos
                print(v)
                swap += 1
                print("swap")
                print(i)
                print("*****")
                i -= 1
                
        return swap

# Example usage
solution = Solution()
nums = [13,1,5,3,6,11,10]
print(solution.minSwaps(nums))  # Output: 2

# 7
# 13 1 5 3 6 11 10