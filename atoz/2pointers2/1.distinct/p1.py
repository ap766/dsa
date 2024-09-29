#Find the longest substring with k unique characters in a given string
# Last Updated : 24 Apr, 2023
# Given a string you need to print longest possible substring that has exactly M unique characters. If there is more than one substring of longest possible length, then print any one of them.

# Examples: 

# Input: Str = “aabbcc”, k = 1
# Output: 2

#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        mpp={}
        l=0
        r=0
        n=len(s)
        maxlen=-1
        
        while r<n:
            if s[r] in mpp:
               mpp[s[r]]+=1
            else:
               mpp[s[r]]=1
               
            if len(mpp)>k:
                mpp[s[l]]-=1
                if mpp[s[l]]==0:
                    del mpp[s[l]]
                l+=1
                
            if len(mpp)==k:
                maxlen=max(maxlen,r-l+1)
                
            r+=1
        return maxlen
                
                