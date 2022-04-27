def unite_unique(list_of_numbers):
    '''
    Find unique value in list
    '''
    new=[]
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] not in new:
            new.append(list_of_numbers[i])
    return new

lis=[1,2,4,3,1,2]
print(unite_unique(lis))
