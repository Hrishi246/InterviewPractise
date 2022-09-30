import string


def is_pangram(s):
    alpha_array = []
    for each in s:
        if each != " " and each not in alpha_array and each.isalpha():
            alpha_array.append(each.lower())

    if len(alpha_array) == 26:
        return True
    return False

is_pangram("")