def elemnt(lis,num):
    '''
    Drop number in list
    '''
    new=[]
    
    for i in range(len(lis)):
        if lis[i]>=num:
            new.append(lis[i])
    return new

li=[1,2,3,4,5,6,1,2]
print(elemnt(li,4))




