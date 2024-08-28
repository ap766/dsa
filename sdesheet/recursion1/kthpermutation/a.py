class Solution:
    def partition(self, s: str) :
        ans = []

        def ispalin(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def recur(ind, sub):
            if ind == len(s):  # Corrected to check against the length of s
                ans.append(sub[:])  # Correctly append a copy of sub
                return

            for i in range(ind, len(s)):
                if ispalin(ind, i):
                    recur(i + 1, sub + [s[ind:i+1]])  # Correctly pass a new list with the substring added

        recur(0, [])
        return ans
    
s=Solution()
