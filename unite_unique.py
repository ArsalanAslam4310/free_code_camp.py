def unite_unique(*lists):
    '''
    Find unique value in list
    '''
    new = []
    for lis in lists:
        for num in lis:
            if num not in new:
                new.append(num)

    return new


print(unite_unique([1, 3, 2, 3], [5, 2, 1, 4], [2, 1]))

