                            
from typing import List

def maxScore(cardPoints: List[int], k: int) -> int:
    
    lsum = 0
    rsum = 0
    maxSum = 0
    rIndex = len(cardPoints) - 1
  
    for i in range(k):
        lsum += cardPoints[i]    
    maxSum = lsum
    
  
    for i in range(k - 1, -1, -1):
        lsum -= cardPoints[i]
        rsum += cardPoints[rIndex]
      
        rIndex -= 1
        maxSum = max(maxSum, lsum + rsum)
    
    return maxSum
