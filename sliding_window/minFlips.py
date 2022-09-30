def minFlips(s):
    n = len(s)
    s = s + s
    alt1 = "10" * n
    alt2 = "01" * n
    diff1 = 0
    diff2 = 0
    res = len(s)
    l = 0
    for r in range(len(s)):
        if s[r] != alt1[r]:
            diff1 = diff1 + 1
        if s[r] != alt2[r]:
            diff2 = diff2 + 1
        if (r-l+1) > n:
            if s[l] != alt1[l]:
                diff1 = diff1 - 1
            if s[l] != alt2[l]:
                diff2 = diff2 - 1

            l = l + 1

        if (r-l+1) == n:
            res = min(res, diff1, diff2)

    return res

res = minFlips("111000")
print(res)


