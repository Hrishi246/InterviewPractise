def combinationSum(candidates, target):

    def dfs(candidates, target):
        if target == 0:
            return [[]]
        if target < 0:
            return None

        final = []
        for i,c in enumerate(candidates):
            rem = target - c
            res = dfs(candidates[i:], rem)
            if res is not None:
                res = list(map(lambda x : x + [c],res))
                final = final + res
        return final



    return dfs(candidates, target)


print(combinationSum([2,3,5],8))
