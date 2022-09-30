# 0,1,1,2,3,5,8,13
def sum_fibonacci(n):
    fib_arr = []
    for i in range(n):
        if i == 0:
            fib_arr.append(i)
        elif i == 1:
            fib_arr.append(i)
        else:
            fib_arr.append(fib_arr[i-1] + fib_arr[i-2])

    return sum(fib_arr)

print(sum_fibonacci(8))