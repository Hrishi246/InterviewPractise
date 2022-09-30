def letterCombinations(digits):
    res = []
    ref = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def backtrack(i, curr):
        if len(curr) == len(digits):
            res.append(curr)
            return
        for c in ref[digits[i]]:
            backtrack(i+1,curr+c)

    if digits:
        backtrack(0,"")

    return res

print(letterCombinations("23"))