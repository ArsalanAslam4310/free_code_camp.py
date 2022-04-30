def smallest_commons(arr: list[int]) -> int:
    flag = False
    start = arr[0]
    end = arr[1]
    num = end
    if arr[0] > arr[1]:
        start = arr[1]
        end = arr[0]
        num = end

    while True:
        for i in range(start, end+1):
            if num % i != 0:
                flag = False
                break
            else:
                flag = True
        if flag:
            break
        num += 1
    return num


print(smallest_commons([18, 23]))
