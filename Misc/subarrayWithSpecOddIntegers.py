def solve(array, m):
    left = 0
    odd = 0
    for right in range(len(array)):
        while array[right] % 2 != 0 and odd < m+2:
            odd = odd + 1
            if odd == m:
                right_first = right
            if odd == m+1:
                right_next = right

        while array[left] %2 != 0:
            left = left + 1

        left_next = left

    return






solve([4,1,3,2,5,6,2,2,3],3)
