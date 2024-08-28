#generate all in order
#linear search to search for it
#the next index

# ...................................
# 1)Recursive Approach:

# The key idea is to use recursion to build each permutation step-by-step.
# We maintain a data structure (ds) to store the current permutation being constructed.
# A frequency array (freq) helps keep track of which elements have been used in the current permutation.

# 2)Base Case:

# When the size of the ds matches the size of the input list nums, a complete permutation is formed.
# We copy this permutation into the result list (ans).



#CODE

#we have a ds to pick up elements and store it
#we have a freq array to keep track of the elements which have been used

#how we pick up elements - we loop 
#We check if its picked and accordingly add 
#and then we remove it 
# ......................
#Time Complexity n! permutation

# Number of Recursive Calls:
# Each call to recurPermute explores all elements of nums to see if they can be added to the current permutation (ds).
# In the worst case, for the first element, we have N choices (where N is the length of nums).
# After choosing the first element, we have  N−1 choices for the second element, and so on.This leads to a total of N×(N−1)×(N−2)×…×1=N! permutations.

# Work Done Per Recursive Call:

# For each recursive call, we loop through all 
# N elements to check which element can be added to the current permutation.
# In the process, each call performs operations such as adding an element to ds, marking it in freq, making a recursive call, and then backtracking (removing the element from ds and unmarking it in freq).
# Each of these operations is 
# O(1), but they are performed 
# N times in each call.


#Stack - O(N) for ds and frq array - O(N) We are ignoring the auxillary space  for recursion
