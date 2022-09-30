def how_sum(target, numbers):
    dp = [None] * (target + 1)
    dp[0] = []
    for i in range(target + 1):
        if dp[i] is not None:
            for num in numbers:
                if (i+num) <= target:
                    dp[i + num] = dp[i] + [num]

    return dp[target]

if __name__ == '__main__':
    print(how_sum(7,[2,3]))
    print(how_sum(7,[5,3,4,7]))
    print(how_sum(7,[2,4]))
    print(how_sum(8,[2,3,5]))
    print(how_sum(300,[7,14]))

