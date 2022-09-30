def removeDuplicates(s,k):
    stack = []  # [letter, duplicateL]
    i = 0
    res = ""
    while i < len(s):
        while stack and i < len(s) and stack[-1][0] == s[i]:
            stack.append([s[i], stack[-1][1] + 1])
            if stack[-1][1] == k:
                for j in range(k):
                    stack.pop()
            i = i + 1
        if i < len(s):
            stack.append([s[i], 1])
        i = i + 1

    for each in stack:
        res = res + each[0]

    return res

res = removeDuplicates("pbbcggttciiippooaais",2)
print(res)