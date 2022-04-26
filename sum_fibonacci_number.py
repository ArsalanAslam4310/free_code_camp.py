def fibonachi_number(num):
    '''
    sum fibonacci numbers
    '''
    prev_num = 1
    curr_num = 1
    next_num = prev_num + curr_num
    sum = 0
    sum += prev_num+curr_num

    while next_num <= num:
        prev_num = curr_num
        curr_num = next_num
        next_num = prev_num + curr_num
        if curr_num % 2 != 0:
            sum += curr_num
    return sum


print(fibonachi_number(1))
