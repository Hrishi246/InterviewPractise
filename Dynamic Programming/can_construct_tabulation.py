def can_construct(target, wordbank):
    dp = [False]*(len(target)+1)
    dp[0] = True
    for i in range(len(target)+1):
        if dp[i]:
            for word in wordbank:
                if (i+len(word)) <= len(target) and target[i:].startswith(word):
                    dp[i+len(word)] = True

    return dp[len(target)]

if __name__ == '__main__':
    print(can_construct("abcdef",["ab","abc","cd","def","abcd"]))
    print(can_construct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
    print(can_construct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
    print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee","eeeeee"]))
    print(can_construct("helloworld",["hel","lo","worl","d"]))
