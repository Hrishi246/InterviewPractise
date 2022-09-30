from collections import defaultdict
def totalFruit(fruits):
    f = 0
    s = 1
    unique_counter = defaultdict(int)
    unique_counter[fruits[0]] = 1
    max_val = 1
    while s < len(fruits):
        if fruits[s] in unique_counter:
            unique_counter[fruits[s]] += 1
            max_val = max(max_val, s - f + 1)
            s += 1
        else:
            if len(unique_counter) < 2:
                unique_counter[fruits[s]] = 1
                max_val = max(max_val, s - f + 1)
                s += 1
            else:
                unique_counter[fruits[f]] -= 1
                if unique_counter[fruits[f]] == 0:
                    del unique_counter[fruits[f]]
                f += 1

    return max_val

print(totalFruit([1,2,3,2,2]))