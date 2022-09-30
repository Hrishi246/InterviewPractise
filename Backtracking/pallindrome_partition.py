def partition(s):
    if s == "":
        return [[]]
    if len(s) == 1:
        return [[s]]
    final_res = []
    for i in range(len(s)):
        if s[:i + 1] == s[:i + 1][::-1]:
            res = partition(s[i+1:])
            res = list(map(lambda x : [s[:i+1]] + x, res))
            final_res = final_res + res

    return final_res

print(partition("aab"))
