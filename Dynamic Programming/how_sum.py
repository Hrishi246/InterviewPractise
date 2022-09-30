

def how_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        rem = target_sum - num
        res = how_sum(rem, numbers, memo)
        if res is not None:
            res.append(num)
            memo[target_sum] = res
            return memo[target_sum]

    memo[target_sum] = None
    return None

if __name__ == '__main__':
    print(how_sum(7,[2,3]))
    print(how_sum(7,[5,3,4,7]))
    print(how_sum(7,[2,4]))
    print(how_sum(8,[2,3,5]))
    print(how_sum(300,[7,14]))
