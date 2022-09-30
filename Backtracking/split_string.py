def if_difference_one(res_one, num):

    diff_list = []
    n = res_one.pop()
    if abs(n-num) == 1:
        diff_list.append(True)
    return diff_list

def split_string(s):

    if s == "":
        return [[]]
    # fin_res = []
    for i in range(len(s)-1):
        if abs(int(s[:i+1]) - int(s[i+1:])) == 1:
            res = split_string(s[i+1:])
            if res:
                return True

    return False

print(split_string("050043"))


