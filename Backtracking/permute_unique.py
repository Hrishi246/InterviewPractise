from collections import Counter

def permute_unique(nums):
    res = []
    perm = []
    count = Counter(nums)

    def dfs():
        if len(perm) == len(nums):
            res.append(perm.copy())
            return
        for n in count:
            if count[n] > 0:
                perm.append(n)
                count[n] = count[n] - 1
                dfs()
                count[n] = count[n] + 1
                perm.pop()

    dfs()
    return res


print(permute_unique(nums = [1,1,2]))
