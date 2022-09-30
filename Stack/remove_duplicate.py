def removeDuplicates(s):
    stack = []
    i = 0
    while i < len(s):
        while stack and i < len(s) and stack[-1] == s[i]:
            stack.pop()
            i = i + 1
        if i < len(s):
            stack.append(s[i])
        i = i + 1

    return "".join(stack)

res= removeDuplicates("aababaab")
print(res)