def removekdigits(num,k):
    stack = [] #monotonic increasing stack
    for n in num:
        while stack and stack[-1] > n and k > 0:
            stack.pop()
            k = k - 1
        stack.append(n)

    while stack and k > 0:
        stack.pop()
        k = k - 1

    res = "".join(stack).lstrip("0")
    return "0" if res == "" else res

print(removekdigits("1432219",3))
