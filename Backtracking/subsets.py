def subsets(nums):

    def dfs():
        if len(nums) == 0:
            return [[]]
        n = nums.pop()
        res = dfs()
        res = res + list(map(lambda x : x + [n], res))
        nums.append(n)

        return res


    return dfs()



print(subsets(["a","b"]))



