def maxFreq(nums, k):
    nums.sort()
    l,r = 0,0
    res, total = 0,0
    while r < len(nums):
        total = total + nums[r]
        while (nums[r] * (r-l+1)) > total + k:
            total =  total - nums[l]
            l = l + 1

        res = max(res, r -l + 1)
        r = r + 1

    return res


print(maxFreq(nums = [1,4,8,13], k = 5))