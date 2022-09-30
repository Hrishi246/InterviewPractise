def searchRange(nums, target):
    if not nums:
        return [-1, -1]

    left = 0
    right = len(nums) - 1

    while left <= right:

        if nums[left] > target or nums[right] < target:
            return [-1, -1]

        mid = (left + right) // 2

        if nums[mid] == target:

            low = mid
            while low > 0 and nums[low - 1] == target:
                low -= 1

            high = mid
            while high < len(nums) - 1 and nums[high + 1] == target:
                high += 1

            return [low, high]

        if nums[mid] < target:
            left = mid + 1

        if nums[mid] > target:
            right = mid - 1

print(searchRange([2,2],2))