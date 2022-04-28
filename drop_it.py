def drop_elements(lis, func):
    '''
    Drop number in list
    '''
    new = []
    for num in lis:
        if func(num):
            new.append(num)
    return new


lis = [1, 2, 3, 4, 5, 6, 1, 2]
lis = drop_elements(lis, lambda n: n >= 3)
print(lis)



