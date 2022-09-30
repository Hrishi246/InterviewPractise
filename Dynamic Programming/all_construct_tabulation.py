def all_construct(target, wordbank):
    dp = [[]] * (len(target)+1)
    dp[0] = [[]]
    for i in range(len(target)+1):
        if dp[i] != []:
            for word in wordbank:
                if (i+len(word)) <= len(target) and target[i:].startswith(word):
                    dp[i+len(word)] = dp[i+len(word)] + list(map(lambda ele : ele + [word], dp[i]))
    return dp[len(target)]

if __name__ == '__main__':
    print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
    print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
    print(all_construct("hello", ["this", "is", "hrishikesh"]))
    print(all_construct("yellowstonenationalpark", ["yellow", "stone", "one", "st", "nation", "national", "al", "park"]))
