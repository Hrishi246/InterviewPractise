def fib(n):
    fib_numbers  = [0 for i in range(n+1)]
    fib_numbers[1] = 1
    for i in range(len(fib_numbers)-1):
        fib_numbers[i+1] = fib_numbers[i] + fib_numbers[i+1]
        if (i+2) < len(fib_numbers):
            fib_numbers[i+2] = fib_numbers[i] + fib_numbers[i+2]

    return fib_numbers[n]


if __name__ == '__main__':
    print(fib(6))
    print(fib(7))
    print(fib(8))
    print(fib(50))
