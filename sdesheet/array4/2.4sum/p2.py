


from typing import List
import itertools

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    n = len(nums)
    st = set()

    # checking all possible quadruplets:
    for i in range(n):
        for j in range(i+1, n):
            hashset = set()
            for k in range(j+1, n):
                # taking bigger data type to avoid integer overflow:
                sum_ = nums[i] + nums[j] + nums[k]
                fourth = target - sum_
                if fourth in hashset:
                    temp = [nums[i], nums[j], nums[k], fourth]
                    temp.sort()
                    st.add(tuple(temp))
                # put the kth element into the hashset:
                hashset.add(nums[k])

    ans = [list(t) for t in st]
    return ans


if __name__ == '__main__':
    nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
    target = 9
    ans = fourSum(nums, target)
    print("The quadruplets are:")
    for it in ans:
        print("[", end="")
        for ele in it:
            print(ele, end=" ")
        print("]", end=" ")
    print()

