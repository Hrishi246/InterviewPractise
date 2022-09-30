def merge(intervals):
    window = intervals[0]
    res = []

    for i in range(len(intervals) - 1):
        if window[1] > intervals[i + 1][0]:
            res.append([window[0], intervals[i + 1][1]])
            window = [window[0], intervals[i + 1][1]]
        else:
            res.append(intervals[i + 1])
            window = intervals[i + 1]

    return res

merge([[1,3],[2,6],[8,10],[15,18]])