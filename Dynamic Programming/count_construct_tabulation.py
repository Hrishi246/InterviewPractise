def count_construct(target, wordbank):
    dp = [0] * (len(target)+1)
    dp[0] = 1
    for i in range(len(target)+1):
        if dp[i] != 0:
            for word in wordbank:
                if (i + len(word)) <= len(target) and target[i:].startswith(word):
                    dp[i + len(word)] =  dp[i + len(word)] + dp[i]

    return dp[len(target)]

if __name__ == '__main__':
    print(count_construct("purple",["purp","p","ur","le","purpl"]))
    print(count_construct("abcdef",["ab","abc","cd","def","abcd"]))
    print(count_construct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
    print(count_construct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
    print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee","eeeeee"]))
