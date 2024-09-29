class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        l=0
        r=0
        n=len(s)
        h=[-1]*255
        while r<n:
            if(h[ord(s[r])]!=-1):
               if h[ord(s[r])]>=l:
                    l=h[ord(s[r])]+1
            maxlen=max(maxlen,r-l+1)
            h[ord(s[r])]=r
            r+=1
        return maxlen
    
    