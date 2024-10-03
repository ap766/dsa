from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        
        def recur(last, cur):
            if len(cur) == n:
                ans.append(cur)
                return
            
            if last != "0":
                recur("0", cur + "0")
            
            recur("1", cur + "1")
        
        recur("", "")
        return ans
        
n=3
sol = Solution()
print(sol.validStrings(3))