
def prevSmaller(A):
        ans=[-1]*len(A)
        st=[]     
        for i in range(0,len(A)):
            while st and A[i]<=st[-1]:
                st.pop()
            if st:
                ans[i]=st[-1]
            st.append(A[i])
        return ans
            