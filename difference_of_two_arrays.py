def diff_array(lis1,lis2):
    '''
    difference of two arrays
    '''
    new=[]

    for i in range(len(lis1)):
        if lis1[i] not in lis2:
            new.append(lis1[i])
         if lis2[i] not in lis1
            new.append(lis2)
    return new


print(diff_array(["andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"])) 
