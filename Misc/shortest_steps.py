def shortest_steps_to_num(num):
    step_count = 0
    while num > 1:
        if (num % 2) == 0:
            num = num / 2
            step_count = step_count + 1
        if (num % 2) == 1 and num!= 1:
            num = num - 1
            step_count = step_count + 1

    return step_count

print(shortest_steps_to_num(12))





