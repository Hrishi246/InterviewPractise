def longestConsecutive(nums):
    nums.sort()
    n = len(nums)
    i = 0
    count = 1
    res = []
    print(nums)
    while i <= n - 2:
        while nums[i + 1] == nums[i] + 1 and (i <= n-2):
            i = i + 1
            count = count + 1
        res.append(count)
        count = 1
        i = i + 1
    return max(res)

longestConsecutive([0, 0, 1, 2, 3, 4, 5, 6, 7, 8])