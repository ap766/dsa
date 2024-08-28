# In the question, it is clearly stated that for each case the picked indices i.e. a, b, c, and d must be distinct. This means [arr[1], arr[1], arr[2], arr[3]] is not valid and also remember [arr[1], arr[0], arr[2], arr[3]] and [arr[0], arr[1], arr[2], arr[3]] will be considered same.

class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums) # size of the array
        st = set()

        # checking all possible quadruplets:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        # taking bigger data type
                        # to avoid integer overflow:
                        sum = nums[i] + nums[j]
                        sum += nums[k]
                        sum += nums[l]

                        if sum == target:
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()
                            st.add(tuple(temp))

        ans = [list(x) for x in st]