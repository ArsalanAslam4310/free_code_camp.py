def sum_all(lis):
    '''
    sum all number in range of list value 
    '''
    sum = 0
    
    for i in range(lis[0],lis[1]+1):
        sum = sum +i

    return sum 

lis=[5,10]
print(sum_all(lis))
