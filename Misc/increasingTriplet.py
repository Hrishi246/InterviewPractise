from bisect import *

def increasingTriplet(nums):
    min1, min2 = nums[0], float('inf')
    for i in nums:
        if min2 < i: return True
        if min1 < i:
            min2 = min(min2, i)
        else:
            min1 = i
    return False

increasingTriplet([2,1,5,0,4,6])