def can_sum(sum, numbers, memo={}):
    if sum in memo:
        return memo[sum]
    if sum < 0:
        return False
    if sum == 0:
        return True
    for num in numbers:
        rem = sum - num
        if can_sum(rem, numbers, memo):
            memo[sum] = True
            return True

    memo[sum] = False
    return False


# print(can_sum(7, [2,3]))
# print(can_sum(7, [5,3,4,7]))
# # print(can_sum(7, [2,4]))
# print(can_sum(8, [2,3,5]))
print(can_sum(300, [7,14]))