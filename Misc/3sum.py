def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right] + nums[i]
            if sum == 0:
                if [nums[i], nums[left], nums[right]] not in res:
                    res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1
    return res

threeSum([-1,0,1,2,-1,-4])
