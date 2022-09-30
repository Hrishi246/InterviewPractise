def minSubArrayLen(target, nums):
    res = 0
    start, end = 0, 0
    currsum = nums[end]
    while start < len(nums) and end < len(nums) and start <= end:
        if currsum < target:
            end = end + 1
            if end < len(nums):
                currsum = currsum + nums[end]
        if currsum > target:
            if res == 0:
                res = end - start + 1
            else:
                res = min(res, end - start + 1)
            currsum = currsum - nums[start]
            start = start + 1
        if currsum == target:
            if res == 0:
                res = end - start + 1
            else:
                res = min(res, end - start + 1)
            end = end + 1
            if end < len(nums):
                currsum = currsum + nums[end]
            currsum = currsum - nums[start]
            start = start + 1

    return res

res= minSubArrayLen( target = 4, nums = [1,4,4])
print(res)