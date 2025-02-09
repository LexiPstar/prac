# class Solution:
#     def huiwenchuan(self, s: str) -> bool:
#         sgood = "".join(ch.lower() for ch in s if ch.isalnum())
#         return sgood == sgood[::1]
# s = "aba"
# print(Solution().huiwenchuan(s))
# 快排
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 选择中间元素作为基准
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# 示例
arr = [3, 6, 8, 10, 1, 2, 1]
print("快速排序:", quick_sort(arr))


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if i < len(left) and j < len(right):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# 示例
arr = [3, 6, 8, 10, 1, 2, 1]
print("归并排序:", merge_sort(arr))


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# 示例
arr = [3, 6, 8, 10, 1, 2, 1]
print("插入排序:", insertion_sort(arr))


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


# 示例
arr = [3, 6, 8, 10, 1, 2, 1]
print("希尔排序:", shell_sort(arr))


def dual_pivot_quick_sort(arr, low, high):
    if low < high:
        lp, rp = partition(arr, low, high)
        dual_pivot_quick_sort(arr, low, lp - 1)
        dual_pivot_quick_sort(arr, lp + 1, rp - 1)
        dual_pivot_quick_sort(arr, rp + 1, high)


def partition(arr, low, high):
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    pivot1 = arr[low]
    pivot2 = arr[high]
    i = low + 1
    j = high - 1
    k = low + 1

    while k <= j:
        if arr[k] < pivot1:
            arr[k], arr[i] = arr[i], arr[k]
            i += 1
        elif arr[k] >= pivot2:
            while arr[j] > pivot2 and k < j:
                j -= 1
            arr[k], arr[j] = arr[j], arr[k]
            j -= 1
            if arr[k] < pivot1:
                arr[k], arr[i] = arr[i], arr[k]
                i += 1
        k += 1
    i -= 1
    j += 1
    arr[low], arr[i] = arr[i], arr[low]
    arr[high], arr[j] = arr[j], arr[high]
    return i, j


# 示例
arr = [3, 6, 8, 10, 1, 2, 1]
dual_pivot_quick_sort(arr, 0, len(arr) - 1)
print("双路快排:", arr)


def three_way_quick_sort(arr, low, high):
    if low < high:
        lt, gt = partition(arr, low, high)
        three_way_quick_sort(arr, low, lt - 1)
        three_way_quick_sort(arr, gt + 1, high)


def partition(arr, low, high):
    pivot = arr[low]
    lt = low
    gt = high
    i = low + 1
    while i <= gt:
        if arr[i] < pivot:
            arr[i], arr[lt] = arr[lt], arr[i]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt


# 示例
arr = [3, 6, 8, 10, 1, 2, 1]
three_way_quick_sort(arr, 0, len(arr) - 1)
print("三路快排:", arr)
