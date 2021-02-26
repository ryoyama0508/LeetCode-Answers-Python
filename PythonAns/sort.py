l = [1, 6, 4, 8, 3, 5, 9, 2, 10, 7]


def bubble_sort(nums):
    check = True
    while check:
        check = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]  # the same as tmp
                check = True
    return nums


def selection_sort(nums):
    for swap_p in range(len(nums)):
        m_pos = nums.index(min(nums[swap_p:]))
        nums[swap_p], nums[m_pos] = nums[m_pos], nums[swap_p]

    return nums


""" print(bubble_sort(l)) """

""" print(selection_sort(l)) """

print(l[1:], l[:1])
