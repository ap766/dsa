class Solution:
    def threeSum(self, arr):
        st = set()
        n=len(arr)

        for i in range(n):
            hashset = set()
            for j in range(i + 1, n):
                # Calculate the 3rd element:
                third = -(arr[i] + arr[j])

                # Find the element in the set:
                if third in hashset:
                    temp = [arr[i], arr[j], third]
                    temp.sort()
                    st.add(tuple(temp))
                hashset.add(arr[j])

        # store the set in the answer:
        ans = list(st)
        return ans