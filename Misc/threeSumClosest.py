def threeSumClosest(nums, target):
    nums.sort()
    min_diff = abs(target - (nums[0] + nums[1] + nums[2]))
    res = nums[0] + nums[1] + nums[2]

    for i, num in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            actual = num + nums[l] + nums[r]
            if actual == target:
                return actual
            elif actual < target:
                if target - actual <= min_diff:
                    min_diff = target - actual
                    res = actual
                l = l + 1
            else:
                if actual - target <= min_diff:
                    min_diff = actual - target
                    res = actual
                r = r - 1

    return res

print(threeSumClosest([-1,2,1,-4], 1))