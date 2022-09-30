# def insert(intervals, newInterval):
#     # Trim out intervals that are mutually exclusive to the new interval
#     head = [item for item in intervals if item[1] < newInterval[0]]
#     tail = [item for item in intervals[::-1] if item[0] > newInterval[1]][::-1]
#
#     # Find the boundary of the new interval using the remaining intervals after separating head and tail
#     rem = intervals[len(head):len(intervals) - len(tail)]
#     if len(rem) != 0:
#         newInterval[0] = min(newInterval[0], rem[0][0])
#         newInterval[1] = max(newInterval[1], rem[-1][1])
#
#     return head + [newInterval] + tail
#
# insert(intervals = [[1,3],[6,9]], newInterval = [2,5])
arr = [3,7,8]
arr.remove(7)
print(arr)