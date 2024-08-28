class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        
        i=0
        j=0
        
        ind2=(len(nums1)+len(nums2))//2 #2nd even is the odd
        ind1=ind2-1 #the first even
        m=len(nums1)
        n=len(nums2)
        final=m+n
        ind1e1=-1
        ind2e2=-1
        
        cnt=0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                if cnt==ind1:
                   ind1e1=nums1[i]
                   
                if cnt==ind2:
                   ind2e2=nums1[i]
                  
                cnt+=1
                i+=1
            else:
                if cnt==ind1:
                    ind1e1=nums2[j]
                 
                if cnt==ind2:
                    ind2e2=nums2[j]
                cnt+=1
                j+=1
            
                
        while i<m:
        
                if cnt==ind1:
                   ind1e1=nums1[i]
                if cnt==ind2:
                   ind2e2=nums1[i]
                i+=1
                cnt+=1
                
        while j<n:
        
                if cnt==ind1:
                   ind1e1=nums2[j]
                if cnt==ind2:
                   ind2e2=nums2[j]
                j+=1
                cnt+=1
                
        if final%2==1:
            return float(ind2e2)
        else:
            return (ind1e1+ind2e2)/2.0
        
#Instead of actually merging we just keep checking at those indexees.
