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


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    l_front, l_back = nums[: len(nums) // 2], nums[len(nums) // 2 :]

    l_front = merge_sort(l_front)
    l_back = merge_sort(l_back)

    ret = []
    i, j = 0, 0
    while i < len(l_front) and j < len(l_back):
        if l_front[i] < l_back[j]:
            ret.append(l_front[i])
            i += 1
        else:
            ret.append(l_back[j])
            j += 1

    if i < len(l_front):
        ret += l_front[i:]

    if j < len(l_back):
        ret += l_back[j:]

    return ret


def partition(arr, low, high):
    i = low  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1

    arr[i], arr[high] = arr[high], arr[i]
    print(arr, "piv ends")
    return i


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])


str_list = ["at", "", "", "", "ball", "", "", "car", "", "dad"]
str_list.sort()
print(str_list)