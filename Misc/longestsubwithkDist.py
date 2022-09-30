#find longest substring length with k distinct characters:

def longSubWithKChar(string):
    window_start = 0
    max_length = 0
    ref_dict = {}
    for window_end in range(len(string)):
        if string[window_end] not in ref_dict.keys():
            ref_dict[string[window_end]] = 1
        else:
            ref_dict[string[window_end]] = ref_dict[string[window_end]] + 1
        while len(ref_dict.keys()) > 2:
            ref_dict[string[window_start]] = ref_dict[string[window_start]] - 1
            if ref_dict[string[window_start]] == 0:
                ref_dict.pop(string[window_start])

            window_start = window_start + 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length






print(longSubWithKChar("AAAHHIBC"))