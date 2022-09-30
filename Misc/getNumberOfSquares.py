def get_number_of_squares(n):
    sum = 0
    i = 1
    if n == 1:
        return 0
    while sum < n:
        sum = sum + i ** 2
        if sum >= n:
            i = i - 1
            break
        i = i + 1

    return i

print(get_number_of_squares(5))