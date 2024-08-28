class Solution:
    def largestRectangleArea(self, heights) -> int:
            n = len(heights)
            leftSmall = [0] * n
            rightSmall = [0] * n
            st = []

            #checking on the left
            for i in range(n):
                while st and heights[st[-1]] >= heights[i]:
                    st.pop()
                if not st:
                    leftSmall[i] = 0
                else:
                    leftSmall[i] = st[-1] + 1
                st.append(i)

            # clear the stack to be re-used
            print(leftSmall)
            st.clear()


            #This is simular to the question
            for i in range(n-1, -1, -1):
                while st and heights[st[-1]] >= heights[i]:
                    st.pop()
                if not st:
                    rightSmall[i] = n - 1
                else:
                    rightSmall[i] = st[-1] - 1
                st.append(i)

            maxA = 0
            for i in range(n):
                maxA = max(maxA, heights[i] * (rightSmall[i] - leftSmall[i] + 1))

            return maxA

s=Solution()
print(s.largestRectangleArea([2,1,5,6,2,3])) # 10