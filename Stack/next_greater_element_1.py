def nextGreaterElement(nums1, nums2):
    ref = {}
    res = []
    for each in nums2:
        ref[each] = -1
    for i in range(len(nums2)):
        for j in range(i + 1, len(nums2)):
            if nums2[i] < nums2[j]:
                ref[nums2[i]] = nums2[j]
                break
    for n1 in nums1:
        res.append(ref[n1])

    return res

#using Monotonic Queue
def nextGreaterElementStack(nums1, nums2):
    indexref = {n:i for  i,n in enumerate(nums1)}
    res = [-1] * len(nums1)
    stack = []
    for n2 in nums2:
        if stack == []:
            stack.append(n2)
        elif n2 < stack[-1]:
            stack.append(n2)
        elif n2 > stack[-1]:
            while stack:
                top = stack.pop()
                if top in indexref:
                    res[indexref[top]] = n2
            if n2 in indexref:
                stack.append(n2)
    return res

nextGreaterElementStack([4,1,2],[2,1,3,4])


