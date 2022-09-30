def maxSubArray(nums):
    N = len(nums)
    mx = nums[0]
    cur_sum = nums[0]

    for i in range(1, N):
        cur_sum = max(cur_sum + nums[i], nums[i])
        mx = max(mx, cur_sum)

    return mx

maxSubArray([-2,1,-3,4,-1,2,1,-5,4])