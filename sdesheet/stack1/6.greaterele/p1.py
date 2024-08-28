class Solution:
    def nextGreaterElement(self, nums1, nums2):
        mpp={}
        st=[]
        
        for i in range(0,len(nums1)):
            mpp[nums1[i]]=-1
            
        for i in range(len(nums2)-1,-1,-1):
            while st and nums2[i]>st[-1]:
                   st.pop()
            if st and nums2[i] in nums1:
                   mpp[nums2[i]]=st[-1]
            st.append(nums2[i])
        return mpp.values()
                  
            