 from unsorted_search import linear_search


def destroyer(arr, *nums):
    new = []

    for num in nums:
        while linear_search(arr, num):
            arr.remove(num)

    new.append(arr)
    return new


print(destroyer([1, 2, 3, 1, 2, 3], 2, 3))
