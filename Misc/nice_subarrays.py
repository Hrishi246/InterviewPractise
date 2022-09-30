# Given an array of integers nums and an integer k. A continuous subarray is called nice if
# there are k odd numbers on it.
# Return the number of nice sub-arrays.
#
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

def helper_function(num):
    if num%2 == 0:
        return False
    return True

def numberOfSubarrays(array, k):
    result = []
    first_window = []
    final_index = 0
    count = 0
    final_count = 0
    for i in range(len(array)):
        if count == 3:
            final_index = i - 1
            break

        if helper_function(array[i]):
            first_window.append(array[i])
            count = count + 1

    # final_count = final_count + 1

    for i in range(len(array)-k):
        if len(first_window) == 0:
            continue
        first_window.remove(array[i])
        new_window = first_window
        if (final_index + 1)<len(array) and not (array[final_index + 1]%2 == 0):
            new_window.append(array[final_index + 1])
            final_count = final_count + 1
            final_index = final_index + 1
        else:
            continue

    return final_count



array = [2,4,6]
print(numberOfSubarrays(array, 1))