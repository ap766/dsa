def combinationSum(candidates, target):
    ans = []
    
    def findCombination(i, current_target, ds):
        if i == len(candidates):
            if current_target == 0:
                ans.append(ds[:])
            return
        
        if candidates[i] <= current_target:
            findCombination(i, current_target - candidates[i], ds + [candidates[i]])
        
        findCombination(i + 1, current_target, ds)

    findCombination(0, target, [])
    return ans

candidates = [2, 3, 6, 7]
target = 7
ans = combinationSum(candidates, target)
print("Combinations are: ")
for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j], end=" ")
    print()
